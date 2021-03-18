import sys
from db.dbschemasetup import *
from home.settings import DATABASES


if __name__ == '__main__':
    print("\u200a\u200aObtaining database connection parameters...", end =" ")
    params = setup_connection_params(DATABASES['default'])

    print("\u200a\u200aCreating 'master' schema...", end =" ")
    run_sql_command(params, 'db/master.sql')

    print("\u200a\u200aSetting up 'public' schema...", end =" ")
    run_sql_command(params, 'db/public.sql')

    print("\u200a\u200aCreating 'reports' schema...", end =" ")
    run_sql_command(params, 'db/reports.sql')
