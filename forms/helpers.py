from django.db import connection
from .models import *


# Check if user has been selected to participate in the survey to obtain its information
def check_user_survey_enrolment_data(email):
    cursor = connection.cursor()
    sql_check_user_enrolment = "SELECT * FROM forms_enrolledstudent WHERE email = %s"
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

        enrolled_subjects_position = column_names.index('enrolled_subjects')
        user_data['user_subjects'] = user_enrolment[enrolled_subjects_position]

        return user_data


# Check if the user has previously answered the survey
def check_previous_answer(email):
    cursor = connection.cursor()
    sql_check_previous_evaluation = "SELECT * FROM forms_studentevaluation WHERE email_id = %s"
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
                                        WHERE short_name_id = %s AND degree_id = %s 
                                    """
    subjects_list_of_dicts =  []
    for subject in subjects_list:
        cursor = connection.cursor()
        cursor.execute(sql_get_subject_information, (subject, degree,))
        column_names = [column[0] for column in cursor.description]
        user_enrolment = cursor.fetchone()
        if user_enrolment is not None:
            s_dict = {}

            short_name_position = column_names.index('short_name_id')
            s_dict['short_name'] = user_enrolment[short_name_position]

            long_name_position = column_names.index('long_name')
            s_dict['long_name'] = user_enrolment[long_name_position]

            s_dict['degree'] = degree

            subjects_list_of_dicts.append(s_dict)

    return subjects_list_of_dicts


def save_evaluations(user_evaluation, timestamp):
    level = user_evaluation['level']
    classgroup = user_evaluation['classgroup']
    degree = user_evaluation['degree']

    for subject in user_evaluation['evaluations']:
        question1 = user_evaluation['evaluations'][subject]['question1']
        question2 = user_evaluation['evaluations'][subject]['question2']
        question3 = user_evaluation['evaluations'][subject]['question3']
        question4 = user_evaluation['evaluations'][subject]['question4'] if 'question4' in user_evaluation['evaluations'][subject] else None
        question5 = user_evaluation['evaluations'][subject]['question5'] if 'question5' in user_evaluation['evaluations'][subject] else None
        question6 = user_evaluation['evaluations'][subject]['question6'] if 'question6' in user_evaluation['evaluations'][subject] else None
        opinion = user_evaluation['evaluations'][subject]['opinion']

        e = Evaluation(timestamp=timestamp,
                       subject_id=subject,
                       level=level,
                       classgroup=classgroup,
                       degree_id=degree,
                       question1=question1,
                       question2=question2,
                       question3=question3,
                       question4=question4,
                       question5=question5,
                       question6=question6,
                       opinion=opinion)
        e.save()

def save_user_participation(email, timestamp):
    se = StudentEvaluation(email_id=email, evaluation_timestamp=timestamp)
    se.save()



