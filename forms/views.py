from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *
from django.db import connection
from datetime import datetime
from django.contrib.auth import logout
from .classes import UserEvaluation
from .helpers import *
from django.forms import formset_factory
import json

# Create your views here.

def user_checking(request):
    try:
        cursor = connection.cursor()
        auth_user_id = request.session['_auth_user_id']
        sql_get_user_email = "SELECT email FROM auth_user WHERE id = %s"
        cursor.execute(sql_get_user_email, (auth_user_id,))
        column_names = [column[0] for column in cursor.description]
        user_email = cursor.fetchone()[0]
        request.session['user_email'] = user_email

        # Check if it's an address from the school    
        if '@elpuig.xeill.net' not in user_email :
            # End the user session
            logout(request)
            return HttpResponseRedirect(reverse('forms:wrong_email', args=(user_email,)))
        else:
            # Check if the student has been enrolled for the survey
            user_data = check_user_survey_enrolment_data(user_email)
            if user_data is None:
                # End the user session
                logout(request)
                return HttpResponseRedirect(reverse('forms:not_enrolled', args=(user_email,)))
            else:
                # Check if the student has previously answered the survey
                if check_previous_answer(user_email):
                    # End the user session
                    logout(request)
                    return HttpResponseRedirect(reverse('forms:duplicated_answer', args=(user_email,)))
                else:
                    ue = UserEvaluation(user_email, 
                                        user_data['user_level'],
                                        user_data['user_degree'],
                                        user_data['user_classgroup'],
                                        user_data['user_subjects'])
                    request.session['user_evaluation'] = json.loads(ue.toJson())

                    if user_data['user_level'].lower() == 'cf':
                        return HttpResponseRedirect(reverse('forms:subject_evaluation'))
                    else: 
                        return HttpResponseRedirect(reverse('forms:school_evaluation'))
        
    except:
        return HttpResponseRedirect(reverse('forms:unidentified_user'))


def subject_evaluation(request):
    try:
        ue = request.session['user_evaluation']
        user_subjects_info = get_subjects_list_of_dicts(ue['degree'], ue['subjects'])

        SubjectsFormset = formset_factory(EvaluateSubjectCF, extra=len(user_subjects_info))
        formset = SubjectsFormset(request.POST or None)
        
        # Pass  additional argument with subject info, instantiate in template with subform.initial
        for subform, data in zip(formset.forms, user_subjects_info):
            subform.initial = data

        subjects_evaluations = {}
        if formset.is_valid():
            for pos, form in enumerate(formset):
                subjects_evaluations[user_subjects_info[pos]['short_name']] = form.cleaned_data

            ue['evaluations'] = subjects_evaluations
            request.session['user_evaluation'] = ue

            return HttpResponseRedirect(reverse('forms:counseling_evaluation'))

        context = {'formset': formset}
        return render(request, 'forms/subject_evaluation.html', context)
    
    except:
        return HttpResponseRedirect(reverse('forms:unidentified_user'))


def counseling_evaluation(request):
    try:
        ue = request.session['user_evaluation']

        if request.method == 'POST':
            if '1' in ue['classgroup']:
                questions_form = EvaluateCounselingCF1(request.POST)
            else:
                questions_form = EvaluateCounselingCF2(request.POST)

            if questions_form.is_valid():
                ue['evaluations']['Tutoria'] = questions_form.cleaned_data
                request.session['user_evaluation'] = ue

                return HttpResponseRedirect(reverse('forms:school_evaluation'))
        else:
            if '1' in (ue['classgroup']):
                questions_form = EvaluateCounselingCF1()
            else:
                questions_form = EvaluateCounselingCF2()
            return render(request, 'forms/counseling_evaluation.html',
                        {'questions_form': questions_form})
    
    except:
        return HttpResponseRedirect(reverse('forms:unidentified_user'))


def school_evaluation(request):
    try:
        ue = request.session['user_evaluation']

        if request.method == 'POST':
            if ue['level'].lower() == 'cf':
                questions_form = EvaluateSchoolCF(request.POST)
            else:
                questions_form = EvaluateSchoolESOBatx(request.POST)

            if questions_form.is_valid():
                    ue['evaluations']['Centre'] = questions_form.cleaned_data

                    timestamp = str(datetime.now().strftime("%Y/%m/%d %H:%M:%S:%f"))
                    save_evaluations(ue, timestamp)
                    save_user_participation(ue['email'], timestamp)

                    # End the user session
                    logout(request)
                    
                    return HttpResponseRedirect(reverse('forms:recorded_response'))
        else:
            if ue['level'].lower() == 'cf':
                questions_form = EvaluateSchoolCF()
            else:
                questions_form = EvaluateSchoolESOBatx()
            return render(request, 'forms/school_evaluation.html',
                        {'questions_form': questions_form})   

    except:
        return HttpResponseRedirect(reverse('forms:unidentified_user'))


def recorded_response(request):
    return render(request, 'forms/recorded_response.html')


def wrong_email(request, user_email):
    return render(request, 'errors/wrong_email.html', {'user_email':user_email})


def not_enrolled(request, user_email):
    return render(request, 'errors/not_enrolled.html', {'user_email':user_email})


def duplicated_answer(request, user_email):
    return render(request, 'errors/duplicated_answer.html', {'user_email':user_email})

def unidentified_user(request):
    return render(request, 'errors/unidentified_user.html')
