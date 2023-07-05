from settings_base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'postgres',
        'PASSWORD': '',
        'NAME': 'travis',
        'TEST_NAME': 'travis_test',
    }
}
