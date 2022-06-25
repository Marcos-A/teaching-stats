from django.db import connections
from django.utils import timezone
import os


WRONG_ACCESS_ERROR_LOG = os.path.join(os.path.dirname(__file__), '..', 'log', 'error_log-wrong_access.txt')


# Get authorized user email
def get_user_email(auth_user_id):
    cursor = connections['default'].cursor()
    sql_get_user_email = "SELECT email FROM auth_user WHERE id = %s"
    cursor.execute(sql_get_user_email, (auth_user_id,))
    user_email = cursor.fetchone()[0]

    return user_email


# Check if email belongs to an authorized user
def check_user_authorization(email):
    cursor = connections['reports'].cursor()
    sql_check_user_authorization = "SELECT id FROM staff WHERE email = %s;"
    cursor.execute(sql_check_user_authorization, (email,))
    user_authorization = cursor.fetchone()

    if user_authorization is None:
        return False
    else:
        return True


# Save error log
def log_error(error, data='no data'):
    if error == 'not_authorized':
        with open(WRONG_ACCESS_ERROR_LOG, 'a') as error_log:
            error_log.write("%s, %s, %s" % (str(timezone.now()), 'not_authorized', data) + "\n")

    elif error == 'unidentified_staff':
        with open(WRONG_ACCESS_ERROR_LOG, 'a') as error_log:
            error_log.write("%s, %s, %s" % (str(timezone.now()), 'unidentified_staff', data) + "\n")
