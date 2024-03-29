from django.db import connections, transaction
from django.db.utils import DatabaseError
from django.utils import timezone
import json
import os
import traceback
from .models import *


DB_SAVE_ERROR_LOG = os.path.join(os.path.dirname(__file__), '..', 'log', 'error_log-db_save.txt')
WRONG_ACCESS_ERROR_LOG = os.path.join(os.path.dirname(__file__), '..', 'log', 'error_log-wrong_access.txt')


# Get authorized user email
def get_user_email(auth_user_id):
    sql_get_user_email = "SELECT email FROM auth_user WHERE id = %s"
    try:
        cursor = connections['default'].cursor()
        cursor.execute(sql_get_user_email, (auth_user_id,))
        user_email = cursor.fetchone()[0]
        return user_email
    except(Exception, DatabaseError) as error:
        catch_exception(error)


# Check if user has been selected to participate in the survey to obtain its information
def check_user_survey_enrolment_data(email):
    sql_check_user_enrolment = "SELECT * FROM forms_student WHERE email = %s;"
    try:
        cursor = connections['default'].cursor()
        cursor.execute(sql_check_user_enrolment, (email,))
        column_names = [column[0] for column in cursor.description]
        user_enrolment = cursor.fetchone()

        if user_enrolment is None:
            return None
        else:
            user_data = {}

            user_id_position = column_names.index('id')
            user_data['user_id'] = user_enrolment[user_id_position]

            degree_id_position = column_names.index('degree_id')
            user_data['user_degree_id'] = user_enrolment[degree_id_position]

            level_id_position = column_names.index('level_id')
            user_data['user_level_id'] = user_enrolment[level_id_position]

            level_code_position = column_names.index('level_code')
            user_data['user_level_code'] = user_enrolment[level_code_position]    

            group_id_position = column_names.index('group_id')
            user_data['user_group_id'] = user_enrolment[group_id_position]

            enrolled_subjects_position = column_names.index('subjects')
            user_data['user_subjects'] = user_enrolment[enrolled_subjects_position]

            return user_data
    
    except(Exception, DatabaseError) as error:
        catch_exception(error)


# Check if the user has previously answered the survey
def check_previous_answer(user_id):
    sql_check_previous_evaluation = "SELECT * FROM forms_participation WHERE student_id = %s;"
    try:
        cursor = connections['default'].cursor()
        cursor.execute(sql_check_previous_evaluation, (user_id,))
        user_previous_evaluation = cursor.fetchone()

        if user_previous_evaluation is None:
            return False
        else:
            return True

    except(Exception, DatabaseError) as error:
        catch_exception(error)


# Turn string of subjects as a list of dicts with the complete info about every subject
def get_subjects_list_of_dicts(string_of_subjects, degree_id, group_id):
    subjects_list_of_dicts =  []

    if string_of_subjects is None:
        return subjects_list_of_dicts
    else:
        try:
            subjects_list = [subject.replace(' ', '') for subject in string_of_subjects.split(',')
                            if 'Tutoria' not in subject and 'Centre' not in subject]
            
            sql_get_subject_information = """
                                            SELECT * FROM (
                                                SELECT id, code, name, degree_id, degree_code, degree_name, trainer_id, %s AS group_id
                                                FROM public.forms_subject 
                                                WHERE code = %s and degree_id= %s AND group_id IS NULL
                                                UNION
                                                SELECT *
                                                FROM public.forms_subject 
                                                WHERE code = %s and degree_id=%s AND group_id = %s
                                            ) T WHERE group_id = %s
                                            ORDER BY code, name;
                                        """
            
            for subject in subjects_list:
                cursor = connections['default'].cursor()
                cursor.execute(sql_get_subject_information, (group_id, subject, degree_id, subject, degree_id, group_id, group_id,))
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

        except(Exception, DatabaseError) as error:
            catch_exception(error)


# Check if the student is enrolled in any subject
def check_student_subjects_enrollment(user_subjects):
    enrollment_list = user_subjects.split(',')
    for enrollment in enrollment_list:
        if 'tutoria' not in enrollment.lower() and enrollment.lower() != 'centre':
            return True
    return False


# Get subject id from 'master' schema of database
def get_subject_id(subject_code, degree_id):
    sql = "SELECT id FROM master.subject WHERE code = %s AND degree_id = %s;"
    try:
        cursor = connections['master'].cursor()
        cursor.execute(sql, (subject_code, degree_id,))
        subject_id = cursor.fetchone()[0]
        return subject_id
    except(Exception, DatabaseError) as error:
        catch_exception(error)


# Get subject code from 'master' schema of database
def get_subject_code(subject_id, degree_id):
    sql = "SELECT code FROM master.subject WHERE id = %s AND degree_id = %s;"
    try:
        cursor = connections['master'].cursor()
        cursor.execute(sql, (subject_id, degree_id,))
        subject_code = cursor.fetchone()[0]
        return subject_code
    except(Exception, DatabaseError) as error:
        catch_exception(error)


# Get question id from 'master' schema of database
def get_question_id(sort, level_id, subject_code):
    sql = """
        SELECT id FROM master.question
        WHERE sort = %s AND level_id = %s AND
                topic_id = %s AND disabled IS NULL;
        """
    try:
        cursor = connections['master'].cursor()
        cursor.execute(sql, (sort, level_id, get_topic_id(subject_code)))
        question_id = cursor.fetchone()[0]
        return question_id
    except(Exception, DatabaseError) as error:
        catch_exception(error)


# Get topic id from 'master' schema of database
def get_topic_id(subject_code):
    sql = "SELECT id FROM master.topic WHERE name = %s;"
    if 'tutoria' in subject_code.lower() and '1' in subject_code:
        topic_name = 'Tutoria 1r CF'
    elif 'tutoria' in subject_code.lower() and '2' in subject_code:
        topic_name = 'Tutoria 2n CF'
    elif 'centre' in subject_code.lower():
        topic_name = 'Centre'
    else:
        topic_name = 'Assignatura'
    try:
        cursor = connections['master'].cursor()
        cursor.execute(sql, (topic_name,))
        topic_id = cursor.fetchone()[0]
        return topic_id
    except(Exception, DatabaseError) as error:
        catch_exception(error)


# Get trainer id from 'master' schema of database based on a subject id.
# In case of multiple trainers associated with the same subject,
# the function returns only the first one.
def get_trainer_id(subject_id):
    sql = "SELECT trainer_id FROM master.subject_trainer_group WHERE subject_id = %s;"
    try:
        cursor = connections['master'].cursor()
        cursor.execute(sql, (subject_id,))
        query_result = cursor.fetchone()
        if query_result is not None:
            trainer_id = query_result[0]
        # Subject without assigned trainer
        else:
            trainer_id = None
        return trainer_id
    except(Exception, DatabaseError) as error:
        catch_exception(error)


# Get list of tuples with the questions type and statement assigned to a level and topic
def get_questions_type_and_statement_by_level_and_topic(level_name, topic_name):
    cursor = connections['master'].cursor() 
    sql = """
          SELECT t.name, q.statement FROM master.question q
          LEFT JOIN master.type t
              ON q.type_id = t.id
          WHERE q.level_id = (SELECT id FROM master.level
                              WHERE name = %s)
            AND q.topic_id = (SELECT id FROM master.topic
                              WHERE name = %s)
            AND q.disabled IS NULL
          ORDER BY q.sort ASC;
          """  
    cursor.execute(sql, (level_name, topic_name))
    questions_type_and_statement = cursor.fetchall()
    return questions_type_and_statement


# Save responses to forms_evaluation, forms_answer and forms_participation
def save_responses(user_evaluation):
    try:
        group_id = user_evaluation['group_id']
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
                               group_id=group_id,
                               trainer_id=trainer_id,
                               subject_id=subject_id)
                e.save()

                # Save to forms_answer
                for sort, question in enumerate(user_evaluation['evaluations'][subject], start=1):
                    a = Answer(value=user_evaluation['evaluations'][subject][question],
                               question_id=get_question_id(sort, level_id, subject_code),
                               evaluation_id=e.id)
                    a.save()

            # Save to forms_participation
            id = user_evaluation['id']
            p = Participation(timestamp=timezone.now(), student_id=id)
            p.save()

    # Save data log in case of database saving error
    except Exception as ex:
        log_error(ex, user_evaluation)


# Print exception error message
def catch_exception(e):    
    print(str(e))
    print(traceback.format_exc())    


# Save error log
def log_error(error, data='no data'):
    if error == 'wrong_email':
        with open(WRONG_ACCESS_ERROR_LOG, 'a') as error_log:
            error_log.write("%s, %s, %s" % (str(timezone.now()), 'wrong_email', data) + "\n")
            
    elif error == 'not_enrolled':
        with open(WRONG_ACCESS_ERROR_LOG, 'a') as error_log:
            error_log.write("%s, %s, %s" % (str(timezone.now()), 'not_enrolled', data) + "\n")

    elif error == 'duplicated_answer':
        with open(WRONG_ACCESS_ERROR_LOG, 'a') as error_log:
            error_log.write("%s, %s, %s" % (str(timezone.now()), 'duplicated_answer', data) + "\n")

    elif error == 'unidentified_user':
        with open(WRONG_ACCESS_ERROR_LOG, 'a') as error_log:
            error_log.write("%s, %s, %s" % (str(timezone.now()), 'unidentified_user', data) + "\n")

    elif error == 'empty_survey':
        with open(WRONG_ACCESS_ERROR_LOG, 'a') as error_log:
            error_log.write("%s, %s, %s" % (str(timezone.now()), 'empty_survey', data) + "\n")

    # Database save error
    else:
        # Remove user id to ensure anonimity
        del data['id']
        with open(DB_SAVE_ERROR_LOG, 'a') as error_log:
            error_log.write("%s, %s, %s" % (str(timezone.now()),
                                            error,
                                            json.dumps(data, ensure_ascii=False))
                                            + "\n")
