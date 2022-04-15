import os
from pathlib import Path

import cloudinary

from framework_exam.utils import is_production, is_test

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = os.getenv('DEBUG', 'False') == 'True'
APP_ENVIRONMENT = os.getenv('APP_ENVIRONMENT', 'Development')
SECRET_KEY = os.getenv('SECRET_KEY', 'sk')
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'test-bellary.herokuapp.com').split(' ')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_cleanup.apps.CleanupConfig',
    'framework_exam.web',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'framework_exam.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
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

WSGI_APPLICATION = 'framework_exam.wsgi.application'

DEFAULT_DATABASE_CONFIG = {
    'ENGINE': 'django.db.backends.postgresql',
    'HOST': os.getenv('DB_HOST', None),
    'PORT': os.getenv('DB_PORT', '5432'),
    'NAME': os.getenv('DB_NAME', None),
    'USER': os.getenv('DB_USER', None),
    'PASSWORD': os.getenv('DB_PASSWORD', None),
}

DATABASES = {
    'default': DEFAULT_DATABASE_CONFIG,
}

AUTH_PASSWORD_VALIDATORS = []

if is_production():
    AUTH_PASSWORD_VALIDATORS.extend([
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
    ])

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_ROOT = BASE_DIR / 'static'
STATIC_URL = 'staticfiles/'
STATICFILES_DIRS = (
    BASE_DIR / 'staticfiles',
)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = 'mediafiles/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING_LEVEL = 'DEBUG'

if is_production():
    LOGGING_LEVEL = 'INFO'
elif is_test():
    LOGGING_LEVEL = 'CRITICAL'

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            # DEBUG, WARNING, INFO, ERROR, CRITICAL,
            'level': LOGGING_LEVEL,
            'filters': [],
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': LOGGING_LEVEL,
            'handlers': ['console'],
        }
    }
}

AUTH_USER_MODEL = 'web.AppUser'

cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME', None),
    api_key=os.getenv('CLOUDINARY_API_KEY', None),
    api_secret=os.getenv('CLOUDINARY_API_SECRET', None),
)
