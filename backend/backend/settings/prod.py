from .base import *

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'postgres',
    'USER': 'postgres',
    'PASSWORD': 'pass123',
    'HOST': 'db',  # set in docker-compose.yml
    'PORT': 5432  # default postgres port
}
