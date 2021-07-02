# from .dev import *
from pydjango.settings.dev import *

"""
Settings travis
"""

# https://docs.travis-ci.com/user/database-setup/#postgresql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'travis_ci_test',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}