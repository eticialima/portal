"""
Django settings for portal project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
from decouple import config 
from corsheaders.defaults import default_headers
from django.conf.urls.static import static
# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
STATIC_DIR=os.path.join(BASE_DIR,'static')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DEBUG = config('DEBUG', default=False, cast=bool)

CORS_ALLOW_HEADERS = list(default_headers) + [
    'X-Register',
]

# CORS Config
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = False

# ----------------------------------------------------------
# SSL and Cookies
# ----- Production ----- #
if not DEBUG:
	SECURE_SSL_REDIRECT = True
	ADMINS = [(config('SUPER_USER'), config('EMAIL'))]
	SESSION_COOKIE_SECURE = True
	CSRF_COOKIE_SECURE = True

# Application definition

INSTALLED_APPS = [ 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
 
    # --- 3pack --- # 
    'rest_framework',
    'corsheaders',
    'widget_tweaks',  
    'taggit',

    # --- Accounts --- #
    'accounts',

    # --- My Apps ---#
    'base', 
    'painel',
    'post',
    'home',
    'perfil',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
	'corsheaders.middleware.CorsMiddleware',
	# 'whitenoise.middleware.WhiteNoiseMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django_session_timeout.middleware.SessionTimeoutMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware', 
]

ROOT_URLCONF = 'portal.urls'

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

WSGI_APPLICATION = 'portal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, config('NAME_DB')), 
    }
}

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'pt-br' 
TIME_ZONE = 'America/Sao_Paulo' 
USE_I18N = True 
USE_L10N = True 
USE_TZ = True


# ----------------------------------------------------------
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# produção
STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATIC_URL = '/static/' 
# STATICFILES_DIRS=[STATIC_DIR,]
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/' 

# testes
# STATIC_URL = '/static/'
# STATICFILES_DIRS=[STATIC_DIR,]
# MEDIA_ROOT=os.path.join(BASE_DIR,'media')
# MEDIA_URL = '/media/' 

DATE_INPUT_FORMATS = ('%d/%m/%Y','%d-%m-%Y','%Y-%m-%d')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- Custom User Model --- #
AUTH_USER_MODEL = 'accounts.CustomUser'

# ----------------------------------------------------------
# --- Login Logout User --- #
# LOGIN_URL = 'login'
# LOGIN_REDIRECT_URL = 'index'
# LOGOUT_REDIRECT_URL = 'index'
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'painel'
LOGOUT_REDIRECT_URL = '/'


# --------------#
# --- Email --- #

# --- development --- #
if DEBUG:
	EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
 
# ----------------------------------------------------------
# --- Messages --- #
from django.contrib.messages import constants

MESSAGE_TAGS = {
    constants.ERROR: 'alert-danger',
    constants.WARNING: 'alert-warning',
    constants.DEBUG: 'alert-info',
    constants.SUCCESS: 'alert-success',
    constants.INFO: 'alert-info',
}

