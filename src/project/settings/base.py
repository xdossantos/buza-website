"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 1.11.12.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

from django.urls import reverse_lazy


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a3ifdy4nu!!77g4@gxd13s-%+*fn%cxwn!&s6$28k4i94%w55j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

AUTH_PROFILE_MODULE = 'project.accounts.Profile'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    'taggit',
    'project.accounts',
    'project.boards',
    'project.vote',
    'social_django',

    'tinymce',

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

ROOT_URLCONF = 'project.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries':{
                'vote_tags': 'project.templatetags.vote_tags',
                'board_tags': 'project.templatetags.board_tags',
            },
        },
    },
]


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# paths for static files
STATIC_ROOT = ''
STATIC_URL = '/static/'

# paths for media files
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


LOGIN_REDIRECT_URL = reverse_lazy('all_questions')
LOGIN_URL = reverse_lazy('login')
LOGOUT_URL = reverse_lazy('logout')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'edneciamat@gmail.com'
EMAIL_HOST_PASSWORD = '3109sewagodimo'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',

    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
)
# Facebook key
SOCIAL_AUTH_FACEBOOK_KEY = '354119031706754'
SOCIAL_AUTH_FACEBOOK_SECRET = '76d8ba50e252bf6df5c51fe5847908bc'
