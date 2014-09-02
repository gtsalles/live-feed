import os
from decouple import config
from dj_database_url import parse as db_url


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = os.environ.get('SECRET_KEY', config('KEY', default=''))

DEBUG = bool(os.environ.get('DEBUG', config('DEBUG', default=False)))

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['live-feed.herokuapp.com']


# Application definition

INSTALLED_APPS = (
    'south',
    'suit',
    'haystack',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'feed.urls'

WSGI_APPLICATION = 'feed.wsgi.application'


# Database

DATABASES = {
    'default': db_url(os.environ.get('DATABASE_URL', config('DB_URL',
                                                            default='')))
}

# Internationalization

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Fortaleza'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)

STATICFILES_DIRS = (os.path.join(MEDIA_ROOT, 'static'),)


# Django Suit

SUIT_CONFIG = {
    'ADMIN_NAME': 'Live Feed',
    'SEARCH_URL': '',
}

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

# Haystack

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': os.environ.get('ES_URL', config('ES_URL', default='')),
        'INDEX_NAME': 'livefeed',
        'TIMEOUT': 60,
        'KWARGS': {
            'http_auth': os.environ.get('ES_AUTH')
        }
    },
}


# Celery

BROKER_URL = os.environ.get('REDISCLOUD_URL', config('BROKER_URL', default=''))
CELERY_RESULT_BACKEND = os.environ.get('REDISTOGO_URL', config('RESULT_STORE', default=''))
CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'America/Fortaleza'

# Sendgrid

EMAIL_BACKEND = 'sgbackend.SendGridBackend'
SENDGRID_USER = os.environ.get('SENDGRID_USERNAME', config('SENDGRID_USERNAME', default=''))
SENDGRID_PASSWORD = os.environ.get('SENDGRID_PASSWORD', config('SENDGRID_PASSWORD', default=''))