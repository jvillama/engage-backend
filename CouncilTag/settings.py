"""
Django settings for CouncilTag project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import dj_database_url
import redis

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEST = False
CELERY = False

if os.environ.get("CouncilTag") == 'debug':
    DEBUG = True
if os.environ.get("CouncilTag") == 'test':
    TEST = True
if os.environ.get("CouncilTag") == 'celery':
    CELERY = True
print(DEBUG)
ALLOWED_HOSTS = ['localhost', 'engage-santa-monica.herokuapp.com', 'backend.engage.town',
                 'engage.town', 'engage-backend.herokuapp.com', '127.0.0.1', 'sm.engage.town']
APPEND_SLASH = True
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'CouncilTag.ingest',
    'rest_framework',
    'CouncilTag.api',
    'corsheaders',
    'drf_yasg',
    'drf_openapi',
    'django_celery_beat',
    'CouncilTag.celery',
    'CouncilTag.apps.CouncilTagConfig',
]

CELERY_BROKER_URL = f"redis://{os.environ.get('REDIS_HOSTNAME')}:6379"
CELERY_RESULT_BACKEND = f"redis://{os.environ.get('REDIS_HOSTNAME')}:6379"
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
<<<<<<< HEAD
TIME_ZONE = 'UTC'
USE_TZ = True
r = redis.StrictRedis(
    host=f"{os.environ.get('REDIS_HOSTNAME')}", port=6379, db=1)
=======
ONCE_REDIS_URL = 'redis://localhost:6379/0'
ONCE_DEFAULT_TIMEOUT = 60 * 60  # remove lock after 1 hour in case it was stale
TIME_ZONE='UTC'
USE_TZ=True
r = redis.StrictRedis(host='localhost', port=6379, db=1)
>>>>>>> fa8a77110d1368ed8b005e74f3e9a472f2c9d1ae


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.SessionAuthentication'],
}
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'name': 'Authentication',
            'type': 'apiKey',
            'in': 'header',
        }
    },
    'USE_SESSION_AUTH': True,

}
SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
ROOT_URLCONF = 'CouncilTag.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'CouncilTag.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("POSTGRES_DB"),
        'USER': os.environ.get("POSTGRES_USER"),
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD"),
        'HOST': os.environ.get("POSTGRES_HOSTNAME"),
        'TEST': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get("POSTGRES_DB"),
            'USER': os.environ.get("POSTGRES_USER"),
            'PASSWORD': os.environ.get("POSTGRES_PASSWORD"),
            'HOST': os.environ.get("POSTGRES_HOSTNAME"),
        },
    },
}
# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_REGEX_WHITELIST = (
    r'^(https?://)?(.{2,})?engage\.town$',
    r'^(https?://)?(34.219.49.254)(:443)?$',
    r'^(http://)?(localhost):?(8080)?$',
    r'^(http://)?(127.0.0.1):?(8080)?$',
    r'^(https?://)?engage-santa-monica.herokuapp.com$'
)
AUTHENTICATION_BACKENDS = ['CouncilTag.api.backends.EmailPasswordBackend']
AUTH_USER_MODEL = 'ingest.EngageUser'

CORS_URLS_REGEX = r'^/api/.*$'
