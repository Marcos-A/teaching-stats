from django.db import connections, transaction
from django.utils import timezone
import json
import os
from .models import *


# Check if user has been selected to participate in the survey to obtain its information
def check_user_survey_enrolment_data(email):
    cursor = connections['default'].cursor()
    sql_check_user_enrolment = "SELECT * FROM forms_student WHERE email = %s;"
    cursor.execute(sql_check_user_enrolment, (email,))
    column_names = [column[0] for column in cursor.description]
    user_enrolment = cursor.fetchone()

    if user_enrolment is None:
        return None
    else:
        user_data = {}

        degree_id_position = column_names.index('degree_id')
        user_data['user_degree_id'] = user_enrolment[degree_id_position]

        level_id_position = column_names.index('level_id')
        user_data['user_level_id'] = user_enrolment[level_id_position]

        level_code_position = column_names.index('level_code')
        user_data['user_level_code'] = user_enrolment[level_code_position]    

        classgroup_id_position = column_names.index('classgroup_id')
        user_data['user_classgroup_id'] = user_enrolment[classgroup_id_position]

        enrolled_subjects_position = column_names.index('subjects')
        user_data['user_subjects'] = user_enrolment[enrolled_subjects_position]

        return user_data


# Check if the user has previously answered the survey
def check_previous_answer(email):
    cursor = connections['default'].cursor()
    sql_check_previous_evaluation = "SELECT * FROM forms_participation WHERE email = %s;"
    cursor.execute(sql_check_previous_evaluation, (email,))
    user_previous_evaluation = cursor.fetchone()

    if user_previous_evaluation is not None:
        return True
    else:
        return False


# Turn string of subjects as a list of dicts with the complete info about every subject
def get_subjects_list_of_dicts(string_of_subjects, degree_id):
    subjects_list = [subject.replace(' ', '') for subject in string_of_subjects.split(',')
                     if 'Tutoria' not in subject and 'Centre' not in subject]
    
    sql_get_subject_information = """
                                    SELECT * from forms_subject
                                    WHERE code = %s AND degree_id = %s; 
                                  """
    subjects_list_of_dicts =  []
    for subject in subjects_list:
        cursor = connections['default'].cursor()
        cursor.execute(sql_get_subject_information, (subject, degree_id,))
        column_names = [column[0] for column in cursor.description]
        user_enrolments = cursor.fetchall()
        for enrolment in user_enrolments:
            if enrolment is not None:
                s_dict = {}

                id_position = column_names.index('id')
                trainer_id_position = column_names.index('trainer_id')
                # Subject without assigned trainer
                if enrolment[trainer_id_position] is None:
                    id_trainer_id = str(enrolment[id_position])+\
                                    '.' +\
                                    '0'
                # Subject with assigned trainer
                else:
                    id_trainer_id = str(enrolment[id_position])+\
                                    '.' +\
                                    str(enrolment[trainer_id_position])
                s_dict['subject_id.trainer_id'] = id_trainer_id

                code_position = column_names.index('code')
                s_dict['subject_code'] = enrolment[code_position]

                name_position = column_names.index('name')
                s_dict['subject_name'] = enrolment[name_position]

                subjects_list_of_dicts.append(s_dict)

    return subjects_list_of_dicts


# Get subject id from 'master' schema of database
def get_subject_id(subject_code, degree_id):
    cursor = connections['master'].cursor()
    sql = "SELECT id FROM master.subject WHERE code = %s AND degree_id = %s;"
    cursor.execute(sql, (subject_code, degree_id,))
    subject_id = cursor.fetchone()[0]
    return subject_id


# Get subject code from 'master' schema of database
def get_subject_code(subject_id, degree_id):
    cursor = connections['master'].cursor()
    sql = "SELECT code FROM master.subject WHERE id = %s AND degree_id = %s;"
    cursor.execute(sql, (subject_id, degree_id,))
    subject_code = cursor.fetchone()[0]
    return subject_code


# Get question id from 'master' schema of database
def get_question_id(sort, level_id, subject_code):
    cursor = connections['master'].cursor()
    sql = """
            SELECT id FROM master.question
            WHERE sort = %s AND level_id = %s AND
                  topic_id = %s AND disabled IS NULL;
          """
    cursor.execute(sql, (sort, level_id, get_topic_id(subject_code)))
    question_id = cursor.fetchone()[0]
    return question_id


# Get topic id from 'master' schema of database
def get_topic_id(subject_code):
    if 'tutoria1' in subject_code.lower():
        topic_name = 'Tutoria 1r CF'
    elif 'tutoria2' in subject_code.lower():
        topic_name = 'Tutoria 2n CF'
    elif 'centre' in subject_code.lower():
        topic_name = 'Centre'
    else:
        topic_name = 'Assignatura'
    cursor = connections['master'].cursor()
    sql = "SELECT id FROM master.topic WHERE name = %s;"
    cursor.execute(sql, (topic_name,))
    topic_id = cursor.fetchone()[0]
    return topic_id


# Get trainer id from 'master' schema of database based on a subject id.
# In case of multiple trainers associated with the same subject,
# the function returns only the first one.
def get_trainer_id(subject_id):
    cursor = connections['master'].cursor()
    sql = "SELECT trainer_id FROM master.subject_trainer WHERE subject_id = %s;"
    cursor.execute(sql, (subject_id,))
    query_result = cursor.fetchone()
    if query_result is not None:
        trainer_id = cursor.fetchone()[0]
    # Subject without assigned trainer
    else:
        trainer_id = None
    return trainer_id


# Save responses to forms_evaluation, forms_answer and forms_participation
def save_responses(user_evaluation):
    try:
        classgroup_id = user_evaluation['classgroup_id']
        degree_id = user_evaluation['degree_id']
        level_id =  user_evaluation['level_id']

        with transaction.atomic():
            # Save to forms_evaluation
            for subject in user_evaluation['evaluations']:
                # 'Assignatures'
                if '.' in subject:
                    subject_id = subject.split('.')[0]
                    # Subject without assigned trainer
                    if subject.split('.')[1] == '0':
                        trainer_id = None
                    # Subject with assigned trainer
                    else:
                        trainer_id = subject.split('.')[1]
                    subject_code = get_subject_code(subject_id, degree_id)
                # 'Tutoria' and 'Centre'
                else:
                    subject_code =  subject
                    subject_id = get_subject_id(subject_code, degree_id)
                    trainer_id = get_trainer_id(subject_id)
                e = Evaluation(timestamp=timezone.now(),
                               classgroup_id=classgroup_id,
                               trainer_id=trainer_id,
                               subject_id=subject_id,
                               level_id=level_id)
                e.save()

                # Save to forms_answer
                question_sort = 1
                for question in user_evaluation['evaluations'][subject]:
                    a = Answer(value=user_evaluation['evaluations'][subject][question],
                               question_id=get_question_id(question_sort, level_id, subject_code),
                               evaluation_id=e.id)
                    a.save()
                    question_sort += 1

            # Save to forms_participation
            email = user_evaluation['email']
            p = Participation(timestamp=timezone.now(), email=email)
            p.save()

    # Save data log in case of database saving error
    except Exception as ex:
        log_error(ex, user_evaluation)


# Save error log
def log_error(error, data='no data'):
    if error == 'wrong_email':
        with open(os.path.join(os.getcwd(), 'log', 'error_log-wrong_access.txt'), 'a') as error_log:
            error_log.write("%s, %s, %s" % (str(timezone.now()), 'wrong_email', data) + "\n")
            
    elif error == 'not_enrolled':
        with open(os.path.join(os.getcwd(), 'log', 'error_log-wrong_access.txt'), 'a') as error_log:
            error_log.write("%s, %s, %s" % (str(timezone.now()), 'not_enrolled', data) + "\n")

    elif error == 'duplicated_answer':
        with open(os.path.join(os.getcwd(), 'log', 'error_log-wrong_access.txt'), 'a') as error_log:
            error_log.write("%s, %s, %s" % (str(timezone.now()), 'duplicated_answer', data) + "\n")

    elif error == 'unidentified_user':
        with open(os.path.join(os.getcwd(), 'log', 'error_log-wrong_access.txt'), 'a') as error_log:
            error_log.write("%s, %s, %s" % (str(timezone.now()), 'unidentified_user', data) + "\n")

    # Database save error
    else:
        # Remove email information to ensure anonimity
        del data['email']
        with open(os.path.join(os.getcwd(), 'log', 'error_log-db_save.txt'), 'a') as error_log:
            error_log.write("%s, %s, %s" % (str(timezone.now()),
                                            error,
                                            json.dumps(data, ensure_ascii=False))
                                            + "\n")
