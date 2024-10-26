from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
]

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tasks_service',
        'USER': 'tasks_service',
        'PASSWORD': 'YSEYqLwwTPPAB4WHm1z4',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}