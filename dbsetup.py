import sys
from db.dbschemasetup import run_sql_command, setup_connection_params
from home.settings import DATABASES


def catch_exception(e):    
    print(str(e))    
    sys.exit()


def succeed():
    print('\033[92m' + 'OK' + '\033[0m')


if __name__ == '__main__':
    print("\u200a\u200aObtaining database connection parameters...", end =" ")
    try:
        params = setup_connection_params(DATABASES['default'])
        succeed()
    except Exception as e:
        catch_exception(e)

    print("\u200a\u200aCreating 'master' schema...", end =" ")
    try:
        run_sql_command(params, 'db/master.sql')
        succeed()
    except Exception as e:
        catch_exception(e)

    print("\u200a\u200aSetting up 'public' schema...", end =" ")
    try:
        run_sql_command(params, 'db/public.sql')
        succeed()
    except Exception as e:
        catch_exception(e)

    print("\u200a\u200aCreating 'reports' schema...", end =" ")
    try:
        run_sql_command(params, 'db/reports.sql')
        succeed()
    except Exception as e:
        catch_exception(e)
