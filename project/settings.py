import os
from environs import Env
import dj_database_url


env = Env()
env.read_env()

SECRET_KEY = env('SECRET_KEY')

db_config = env('db_config')

DATABASES = {
    'default': db_config,
}


# DB_ENGINE = 'django.db.backends.postgresql_psycopg2'
# DB_HOST = 'checkpoint.devman.org'
# DB_PORT = '5434'
# DB_NAME = 'checkpoint'
# DB_USER = 'guard'
# DB_PASSWORD = 'osim5'

# DATABASES = {
#     'default': {
#         'ENGINE': env('ENGINE'),
#         'HOST': env('HOST'),
#         'PORT': env('PORT'),
#         'NAME': env('NAME'),
#         'USER': env('USER'),
#         'PASSWORD': env('PASSWORD'),
#     }
# }

INSTALLED_APPS = ['datacenter']

DEBUG = env.bool('DEBUG')

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
