import os
import sys


src_path = os.path.join(os.path.dirname(__file__), '..', 'src')
sys.path.insert(1, src_path)

if 'DJANGO_SETTINGS_MODULE' not in os.environ:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

