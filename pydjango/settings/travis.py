from .dev import *

"""
Settings travis
"""

# https://docs.travis-ci.com/user/database-setup/#postgresql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}