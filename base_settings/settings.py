import os
from decouple import config
from pathlib import Path


# Basic directory settings
PROJECT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# BASE_DIR = os.path.join(PROJECT_DIR, 'CidadaoSmart')
# Por enquanto o base dir será o mesmo que o project dir por que ainda não foram criados pastas exteriores ao projeto
BASE_DIR = PROJECT_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# Secret key
SECRET_KEY = config('SECRET_KEY', default='')

# Debug mode (turn True in development)
DEBUG = config('DEBUG', default=False, cast=bool)

# Hosts settings
ALLOWED_HOSTS = ["*"]
INTERNAL_IPS = [
    "127.0.0.1",
]

# Login/Logout settings
LOGIN_URL = '/login/?next='
LOGOUT_URL = 'logout'

# Media/Static settings
STATIC_URL = "static/"
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# STATIC_ROOT = config('STATIC_ROOT', default=os.path.join(BASE_DIR, 'static'))
MEDIA_ROOT = config('MEDIA_ROOT', default=os.path.join(BASE_DIR, 'media'))

MAX_DOC_UPLOAD_SIZE = 150 * 1024 * 1024  # 150MB
MAX_IMAGE_UPLOAD_SIZE = 5 * 1024 * 1024  # 5MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024  # 10MB

# Auth Settings
AUTH_USER_MODEL = 'accounts.User'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LIB_APPS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_framework',
    'rest_framework_simplejwt',
    'easy_thumbnails',
    'image_cropping',
    'widget_tweaks'
]

PROJECT_APPS = [
    'base.apps.BaseConfig',
    'api.apps.ApiConfig',
    'accounts.apps.AccountConfig'
]

INSTALLED_APPS = DJANGO_APPS + LIB_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'base_settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'base_settings.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
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

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

# Email settings

EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_PORT = config('EMAIL_PORT', cast=int, default=587)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool, default=True)
EMAIL_SEND_USER = config('EMAIL_SEND_USER', cast=str, default='')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', cast=str, default='')
SERVER_EMAIL = config('SERVER_EMAIL', cast=str, default='')
EMAIL_RUNNING = None
EMAIL_SUBJECT_PREFIX = config("EMAIL_SUBJECT_PREFIX", default="[RachAqui]")
EMAIL_USE_LOCALTIME = config("EMAIL_USE_LOCALTIME", cast=bool, default=False)
EMAIL_USE_SSL = config("EMAIL_USE_SSL", cast=bool, default=False)

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = config('TZ', default='America/Fortaleza')

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


