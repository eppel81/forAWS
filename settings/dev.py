# try:
#     from .common import *
# except ImportError:
#     pass

from settings.common import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'forAWS',
        'USER': 'dem',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '',
    }
}
