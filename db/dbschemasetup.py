#!/usr/bin/python3.8
import psycopg2


def run_sql_command(params, sql_file_name):
    with open(sql_file_name, 'r') as sql_file:
        sql_command = sql_file.read()

    conn = None
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql_command)
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()


def setup_connection_params(django_settings_params):
    del django_settings_params['ENGINE']
    del django_settings_params['OPTIONS']
    django_settings_params['dbname'] = django_settings_params.pop('NAME')
    django_settings_params['host'] = django_settings_params.pop('HOST')
    django_settings_params['port'] = django_settings_params.pop('PORT')
    django_settings_params['user'] = django_settings_params.pop('USER')
    django_settings_params['password'] = django_settings_params.pop('PASSWORD')

    return django_settings_params
