"""
Settings travis
"""

# https://docs.travis-ci.com/user/database-setup/#postgresql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': 'postgre',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}