from .base import *

DEBUG = False

DATABASES={
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME': 'blogdb',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '',
    },
}