from django.db import connections, transaction
from django.utils import timezone
import json
import os
from .models import *


# Check if user has been selected to participate in the survey to obtain its information
def check_user_survey_enrolment_data(email):
    cursor = connections['default'].cursor()
    sql_check_user_enrolment = "SELECT * FROM forms_student WHERE email = %s"
    cursor.execute(sql_check_user_enrolment, (email,))
    column_names = [column[0] for column in cursor.description]
    user_enrolment = cursor.fetchone()

    if user_enrolment is None:
        return None
    else:
        user_data = {}

        degree_position = column_names.index('degree_id')
        user_data['user_degree'] = user_enrolment[degree_position]

        classgroup_position = column_names.index('classgroup')
        user_data['user_classgroup'] = user_enrolment[classgroup_position]

        level_position = column_names.index('level')
        user_data['user_level'] = user_enrolment[level_position]

        enrolled_subjects_position = column_names.index('subjects')
        user_data['user_subjects'] = user_enrolment[enrolled_subjects_position]

        return user_data


# Check if the user has previously answered the survey
def check_previous_answer(email):
    cursor = connections['default'].cursor()
    sql_check_previous_evaluation = "SELECT * FROM forms_participation WHERE email = %s"
    cursor.execute(sql_check_previous_evaluation, (email,))
    user_previous_evaluation = cursor.fetchone()

    if user_previous_evaluation is not None:
        return True
    else:
        return False


# Turn string of subjects as a list of dicts with the complete info about every subject
def get_subjects_list_of_dicts(degree, string_of_subjects):
    subjects_list = [subject.replace(' ', '') for subject in string_of_subjects.split(',')]
    
    sql_get_subject_information = """SELECT * from forms_subject
                                     WHERE code = %s AND degree_code = %s 
                                  """
    subjects_list_of_dicts =  []
    for subject in subjects_list:
        cursor = connections['default'].cursor()
        cursor.execute(sql_get_subject_information, (subject, degree,))
        column_names = [column[0] for column in cursor.description]
        user_enrolment = cursor.fetchone()
        if user_enrolment is not None:
            s_dict = {}

            short_name_position = column_names.index('code')
            s_dict['short_name'] = user_enrolment[short_name_position]

            long_name_position = column_names.index('name')
            s_dict['long_name'] = user_enrolment[long_name_position]

            s_dict['degree'] = degree

            subjects_list_of_dicts.append(s_dict)

    return subjects_list_of_dicts


# Save responses to forms_evaluation, forms_answer and forms_participation
def save_responses(user_evaluation):
    try:
        classgroup = user_evaluation['classgroup']
        degree = user_evaluation['degree']
        level_id = get_level_id(user_evaluation['level'])

        with transaction.atomic():
            # Save to forms_evaluation
            for subject in user_evaluation['evaluations']:
                subject_id = get_subject_id(subject, degree)
                e = Evaluation(timestamp=timezone.now(),
                            classgroup=classgroup,
                            subject_id=subject_id,
                            level_id=level_id)
                e.save()

                # Save to forms_answer
                question_id = 1
                for question in user_evaluation['evaluations'][subject]:
                    a = Answer(value=user_evaluation['evaluations'][subject][question],
                            question_id=question_id,
                            evaluation_id=e)
                    a.save()
                    question_id += 1


            # Save to forms_participation
            email = user_evaluation['email']
            p = Participation(timestamp=timezone.now(), email=email)
            p.save()

    # Save data log in case of database saving error
    except Exception as ex:
        log_error(ex, user_evaluation)


# Get level id from 'master' schema of database
def get_level_id(level):
    cursor = connections['master'].cursor()
    sql = "SELECT id FROM master.level WHERE name = %s"
    cursor.execute(sql, (level,))
    level_id = cursor.fetchone()
    return level_id[0]


# Get degree id from 'master' schema of database
def get_degree_id(degree):
    cursor = connections['master'].cursor()
    sql = "SELECT id FROM master.degree WHERE code = %s"
    cursor.execute(sql, (degree,))
    degree_id = cursor.fetchone()
    return degree_id[0]


# Get subject id from 'master' schema of database
def get_subject_id(subject, degree):
    cursor = connections['master'].cursor()
    sql = "SELECT id FROM master.subject WHERE code = %s AND degree_id = %s"
    cursor.execute(sql, (subject, get_degree_id(degree),))
    subject_id = cursor.fetchone()
    return subject_id[0]


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
