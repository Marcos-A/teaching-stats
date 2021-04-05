from json import dumps
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from .helpers import *

# Create your views here.
def staff_checking(request):
    try:
        auth_user_id = request.session['_auth_user_id']
        user_email = get_user_email(auth_user_id)
        request.session['user_email'] = user_email

        # Check if user has been authorised to access the analytics
        if not check_user_authorization(user_email):
            # End the user session
            logout(request)
            return HttpResponseRedirect(reverse('analytics:not_authorized', args=(user_email,)))
        else:
            return HttpResponseRedirect(reverse('analytics:school_analytics'))


    except:
        return HttpResponseRedirect(reverse('analytics:unidentified_staff'))


def school_analytics(request):
    try:
        user_email = request.session['user_email']
        return render(request, 'analytics/school_analytics.html')

    except:
        return HttpResponseRedirect(reverse('analytics:unidentified_staff'))


def counseling_analytics(request):
    try:
        user_email = request.session['user_email']
        return render(request, 'analytics/counseling_analytics.html')

    except:
        return HttpResponseRedirect(reverse('analytics:unidentified_staff'))


def subject_analytics(request):
    try:
        user_email = request.session['user_email']
        return render(request, 'analytics/subject_analytics.html')

    except:
        return HttpResponseRedirect(reverse('analytics:unidentified_staff'))


def adm_analytics(request):
    try:
        user_email = request.session['user_email']
        return render(request, 'analytics/adm_analytics.html')

    except:
        return HttpResponseRedirect(reverse('analytics:unidentified_staff'))


def inf_analytics(request):
    try:
        user_email = request.session['user_email']
        return render(request, 'analytics/inf_analytics.html')

    except:
        return HttpResponseRedirect(reverse('analytics:unidentified_staff'))


def logged_out(request):
    try:
        user_email = request.session['user_email']
        logout(request)
        return render(request, 'analytics/logged_out.html')

    except:
        return HttpResponseRedirect(reverse('analytics:unidentified_staff'))

def not_authorized(request, user_email):
    log_error('not_authorized', user_email)
    return render(request, 'errors/not_authorized.html', {'user_email':user_email})


def unidentified_staff(request):
    log_error('unidentified_staff')
    return render(request, 'errors/unidentified_staff.html')
