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
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}