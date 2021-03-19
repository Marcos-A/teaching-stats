from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *
from django.db import connections
from django.contrib.auth import logout
from .classes import UserEvaluation
from .helpers import *
from django.forms import formset_factory
import json


def user_checking(request):
    try:
        cursor = connections['default'].cursor()
        auth_user_id = request.session['_auth_user_id']
        sql_get_user_email = "SELECT email FROM auth_user WHERE id = %s"
        cursor.execute(sql_get_user_email, (auth_user_id,))
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
                ue = UserEvaluation(id=user_data['user_id'],
                                    level_id=user_data['user_level_id'],
                                    level_code=user_data['user_level_code'],
                                    degree_id=user_data['user_degree_id'],
                                    group_id=user_data['user_group_id'],
                                    subjects=user_data['user_subjects'])
                # Check if the student has previously answered the survey
                if check_previous_answer(user_data['user_id']):
                    # End the user session
                    logout(request)
                    return HttpResponseRedirect(reverse('forms:duplicated_answer', args=(user_email,)))
                else:
                    request.session['user_evaluation'] = json.loads(ue.toJson())
                    # ESO-BTX students only evaluate 'Centre'
                    if 'cf' in user_data['user_level_code'].lower():
                        return HttpResponseRedirect(reverse('forms:subject_evaluation'))
                    else:
                        return HttpResponseRedirect(reverse('forms:school_evaluation'))
        
    except:
        return HttpResponseRedirect(reverse('forms:unidentified_user'))


def subject_evaluation(request):
    try:
        ue = request.session['user_evaluation']
        user_subjects_info = get_subjects_list_of_dicts(ue['subjects'], ue['degree_id'], ue['group_id'])

        SubjectsFormset = formset_factory(EvaluateSubjectCF, extra=len(user_subjects_info))
        formset = SubjectsFormset(request.POST or None)
        
        # Pass additional argument with subject info, instantiate in template with subform.initial
        for subform, data in zip(formset.forms, user_subjects_info):
            subform.initial = data

        subjects_evaluations = {}
        if formset.is_valid():
            for pos, form in enumerate(formset):
                subjects_evaluations[user_subjects_info[pos]['subject_id.trainer_id']] = form.cleaned_data

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
        if 'tutoria1' in ue['subjects'].lower():
            tutoria = 'Tutoria1'
        elif 'tutoria2' in ue['subjects'].lower():
            tutoria = 'Tutoria2'
        # If student is not enrolled in 'Tutoria', ignore 'Tutoria' form
        else:
            return HttpResponseRedirect(reverse('forms:school_evaluation'))


        if request.method == 'POST':
            if tutoria == 'Tutoria1':
                questions_form = EvaluateCounselingCF1(request.POST)
            elif tutoria == 'Tutoria2':
                questions_form = EvaluateCounselingCF2(request.POST)

            if questions_form.is_valid():
                ue['evaluations'][tutoria] = questions_form.cleaned_data
                request.session['user_evaluation'] = ue

                return HttpResponseRedirect(reverse('forms:school_evaluation'))
        else:
            if tutoria == 'Tutoria1':
                questions_form = EvaluateCounselingCF1()
            elif tutoria == 'Tutoria2':
                questions_form = EvaluateCounselingCF2()

            return render(request, 'forms/counseling_evaluation.html',
                        {'questions_form': questions_form})
    
    except:
        return HttpResponseRedirect(reverse('forms:unidentified_user'))


def school_evaluation(request):
    try:
        ue = request.session['user_evaluation']

        if request.method == 'POST':
            if 'cf' in ue['level_code'].lower():
                questions_form = EvaluateSchoolCF(request.POST)
            else:
                questions_form = EvaluateSchoolESOBatx(request.POST)

            if questions_form.is_valid():
                    ue['evaluations']['Centre'] = questions_form.cleaned_data
                    
                    save_responses(ue)
 
                    # End the user session
                    logout(request)
                    
                    return HttpResponseRedirect(reverse('forms:recorded_response'))
        else:
            if 'cf' in ue['level_code'].lower():
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
    log_error('wrong_email', user_email)
    return render(request, 'errors/wrong_email.html', {'user_email':user_email})


def not_enrolled(request, user_email):
    log_error('not_enrolled', user_email)
    return render(request, 'errors/not_enrolled.html', {'user_email':user_email})


def duplicated_answer(request, user_email):
    log_error('duplicated_answer', user_email)
    return render(request, 'errors/duplicated_answer.html', {'user_email':user_email})


def unidentified_user(request):
    log_error('unidentified_user')
    return render(request, 'errors/unidentified_user.html')
