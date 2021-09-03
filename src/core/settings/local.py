import os

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# # Database SQLite3
# # https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DB Elephant
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ypvrcfya',
        'USER': 'ypvrcfya',
        'PASSWORD': 'DAdPHFTtr7v3rYJuDgGN4KGYfEtsWJrF',
        'HOST': 'tuffi.db.elephantsql.com',
        'PORT': '5432',
    }
}
