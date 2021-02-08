from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import EvaluateSchool
from django.db import connection
from datetime import datetime
from .models import StudentEvaluation
from django.contrib.auth import logout


# Create your views here.

def user_checking(request):
    cursor = connection.cursor()
    
    auth_user_id = request.session['_auth_user_id']
    sql_get_user_email = "SELECT email FROM auth_user WHERE id = %s"
    cursor.execute(sql_get_user_email, (auth_user_id,))
    user_email = cursor.fetchone()[0]

    # Check if it's an address from the school    
    if '@elpuig.xeill.net' not in user_email :
        # End the user session
        logout(request)
        return HttpResponseRedirect(reverse('forms:wrong_email', args=(user_email,)))
    else:
        sql_check_user_enrolment = "SELECT * FROM forms_enrolledstudent WHERE email = %s"
        cursor.execute(sql_check_user_enrolment, (user_email,))
        user_enrolment = cursor.fetchone()

        # Check if the student has been enrolled for the survey
        if user_enrolment is None:
            # End the user session
            logout(request)
            return HttpResponseRedirect(reverse('forms:not_enrolled', args=(user_email,)))
        else:
            sql_check_previous_evaluation = "SELECT * FROM forms_studentevaluation WHERE email = %s"
            cursor.execute(sql_check_previous_evaluation, (user_email,))
            user_evaluation = cursor.fetchone()

            # Check if the student has previously answered the survey
            if user_evaluation is not None:
                # End the user session
                logout(request)
                return HttpResponseRedirect(reverse('forms:duplicated_answer', args=(user_email,)))
            else:
                return HttpResponseRedirect(reverse('forms:school_evaluation'))


def school_evaluation(request):
    if request.method == 'POST':
        auth_user_id = request.session['_auth_user_id']
        sql_get_user_email = "SELECT email FROM auth_user WHERE id = %s"
        cursor = connection.cursor()
        cursor.execute(sql_get_user_email, auth_user_id)
        user_email = cursor.fetchone()[0]

        items_form = EvaluateSchool(request.POST)
        if items_form.is_valid():
            cursor = connection.cursor()
            sql_check_previous_evaluation = "SELECT * FROM forms_studentevaluation WHERE email = %s"
            cursor.execute(sql_check_previous_evaluation, (user_email,))
            user_evaluation = cursor.fetchone()

            # Check if the student has previously answered the survey
            if user_evaluation is not None:
                # End the user session
                logout(request)
                return HttpResponseRedirect(reverse('forms:duplicated_answer', args=(user_email,)))
            else:
                sql_get_user_level_and_classgroup = "SELECT level, classgroup FROM forms_enrolledstudent WHERE email = %s"
                cursor.execute(sql_get_user_level_and_classgroup, (user_email,))
                user_level_and_classgroup = cursor.fetchone()
                user_level = user_level_and_classgroup[0]
                user_classgroup = user_level_and_classgroup[1]

                timestamp = str(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
                items_form.record_evaluation(timestamp, user_level, user_classgroup)
                new_student_evaluation = StudentEvaluation(email=user_email,
                                                           evaluation_timestamp=timestamp)
                new_student_evaluation.save()
                
                # End the user session
                logout(request)
                
                return HttpResponseRedirect(reverse('forms:recorded_response'))
    else:
        items_form = EvaluateSchool()
        return render(request, 'forms/school_evaluation.html',
                      {'items_form': items_form})
                      

def recorded_response(request):
    return render(request, 'forms/recorded_response.html')


def wrong_email(request, user_email):
    return render(request, 'errors/wrong_email.html', {'user_email':user_email})


def not_enrolled(request, user_email):
    return render(request, 'errors/not_enrolled.html', {'user_email':user_email})


def duplicated_answer(request, user_email):
    return render(request, 'errors/duplicated_answer.html', {'user_email':user_email})
