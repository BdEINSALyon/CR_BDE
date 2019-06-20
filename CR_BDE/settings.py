"""
Django settings for CR_BDE project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'z5cbd*2bhrphp99b6$5(zex13vky-_x5gx+5g8^8wl&cvsq3-%')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DJANGO_ENV', 'dev') == 'dev'

ALLOWED_HOSTS = [os.getenv('ALLOWED_HOSTS', "cr.bde-insa-lyon.fr")]
if DEBUG:
    ALLOWED_HOSTS.extend(['127.0.0.1'])
    ALLOWED_HOSTS.extend(['localhost'])



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'email_obfuscator',
    'analytical',
    'django_crontab',
    'anymail',
    'crispy_forms',
    'bootstrap_datepicker_plus'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CR_BDE.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'CR_BDE.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3'), conn_max_age=600)
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGOUT_REDIRECT_URL = "/"
LOGIN_REDIRECT_URL ="/"

CRONJOBS = [
    ('0 0 10 * *', 'app.cron.delete_file_orphan'),
    ('0 9 1 * *', 'app.cron.send_cr'),
    ('0 9 26 * *', 'app.cron.send_reminder_sg'),
]

# FIX Variables d'environnement pas présentes dans cron
CRONTAB_COMMAND_PREFIX = '. /tmp/env.txt &&'

ANYMAIL = {
    # (exact settings here depend on your ESP...)
    "MAILGUN_API_KEY": os.getenv('MAILGUN_KEY', ""),
    "MAILGUN_SENDER_DOMAIN": os.getenv('MAILGUN_DOMAIN', 'mg.bde-insa-lyon.fr'),  # your Mailgun domain, if needed
    "SEND_DEFAULTS": {
        "tags": ["cr-bde"],
        "track_clicks": False,
    },
}

EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', "cr@mg.bde-insa-lyon.fr")
SERVER_EMAIL = DEFAULT_FROM_EMAIL

EMAIL_SG = os.getenv('EMAIL_SG', "sg@bde-insa-lyon.fr")
EMAIL_CR = os.getenv('EMAIL_CR', "bde.equipe.cr@led.insa-lyon.fr")

GOOGLE_ANALYTICS_PROPERTY_ID = os.getenv('GOOGLE_ANALYTICS_PROPERTY_ID')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = '/media/'