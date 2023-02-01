import os

import environ
from django.db.utils import ConnectionDoesNotExist

env = environ.Env()
environ.Env.read_env()


def get_host_infos():
    """Returns two arrays: ALLOWED_HOSTS and CSRF_TRUSTED_ORIGINS"""
    allowed_hosts = env('HOSTS', str, 'localhost:127.0.0.1').split(':')

    csrf_trusted_origins = [f'{prot}://{host}'
                            for prot in ['http', 'https']
                            for host in allowed_hosts]

    return allowed_hosts, csrf_trusted_origins


# ALLOWED_HOSTS = ['.guiosoft.info', 'localhost',
#                  'acesso-editoracao.fly.dev', '127.0.0.1']
# CSRF_TRUSTED_ORIGINS = ['https://*.guiosoft.info',
#                         'http://localhost', 'https://localhost',
#                         'https://acesso-editoracao.fly.dev']

def get_databases():
    if sqlite := env('SQLITE_DBCONNECTION'):
        db = dict(
            ENGINE='django.db.backends.sqlite3',
            NAME=sqlite,
            OPTIONS=dict(timeout=10)
        )

        print(
            f'SQLite: {sqlite} - file exists: {os.path.isfile(sqlite)} - dir exists: {os.path.isdir(os.path.dirname(sqlite))}')

    else:
        database = env('DATABASE')
        user = env('DB_USER')
        password = env('DB_PASSWORD')
        host = env('DB_HOST')
        port = env('DB_PORT')
        if database and user and password and host and port:
            db = dict(
                ENGINE='django.db.backends.postgresql_psycopg2',
                NAME=database,
                USER=user,
                PASSWORD=password,
                HOST=host,
                PORT=port
            )
            print(f'PostgreSQL: {db}')
        else:
            raise ConnectionDoesNotExist('NO DATABASE CONNECTION')
    return dict(default=db)


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': env('SQLITE_DBCONNECTION', cast=str,
#                     default='/db/db.sqlite3'),
#         'OPTIONS': {
#             'timeout': 10,
#         }
#     },
#     'pg': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': env('DATABASE'),
#         'USER': env('DB_USER'),
#         'PASSWORD': env('DB_PASSWORD'),
#         'HOST': env('DB_HOST'),
#         'PORT': env('DB_PORT'),
#     }
# }

def get_martor():
    """Returns a tuple (MARTOR_IMGUR_CLIENT_ID, MARTOR_IMGUR_API_KEY)"""
    client_id = env('MARTOR_IMGUR_CLIENT_ID')
    api_key = env('MARTOR_IMGUR_API_KEY')
    return client_id, api_key
