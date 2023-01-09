"""
Django settings for youtube_downloader project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-b$6n=x=&v(rd441guucw*u-gu7t(3n$mi!t&h#3=htido2%zp-'
# with open('/etc/secret_key.txt') as f:
# with open('secret_key.txt') as f:
#     SECRET_KEY = f.read().strip()
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'secret_key.txt')) as f:
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'download.apps.DownloadConfig',
    # 'youtube_downloader',
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

ROOT_URLCONF = 'youtube_downloader.urls'

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

WSGI_APPLICATION = 'youtube_downloader.wsgi.application'
ASGI_APPLICATION = 'youtube_downloader.asgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('POSTGRES_NAME'),
#         'USER': os.environ.get('POSTGRES_USER'),
#         'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
#         'HOST': '127.0.0.1',
#         'PORT': 5432,
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
# STATIC_URL = os.path.join(BASE_DIR, "static/")
# STATIC_URL = str(BASE_DIR)+'/static/'
# STATIC_URL = 'http://127.0.0.1:8080/youtube_downloader/static/'
MEDIA_URL = "/media/"
# STATICFILES_DIRS = (os.path.join(BASE_DIR, ''),)
# STATICFILES_DIRS = (os.path.join(BASE_DIR, ""),)
# STATIC_ROOT = str(BASE_DIR)+"static/"
# STATIC_ROOT = os.path.join(BASE_DIR, "static/")
# MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
# STATIC_ROOT = "staticfiles/"
# STATIC_ROOT = "static"
# STATIC_ROOT = BASE_DIR / 'staticfiles'
# STATIC_ROOT = 'static/'
# print(STATIC_ROOT)
MEDIA_ROOT = BASE_DIR / "media"
# find static
# py manage.py findstatic --verbosity 2 static 
# python manage.py findstatic app.css

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# unicorn RUN
# gunicorn myproject.asgi:application -k uvicorn.workers.UvicornWorker

# hypercorn RUN
# hypercorn myproject.asgi:application
# hypercorn youtube_downloader.asgi:application

# trzeba ffmpeg zainstalować