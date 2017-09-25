"""
WSGI config for tnp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "studentportal.settings")

from django.core.wsgi import get_wsgi_application

from whitenoise.django import DjangoWhiteNoise


application = get_wsgi_application()
application = DjangoWhiteNoise(application)
#smtp_proxy   = "172.31.16.10:8080" #Use this if you have a proxy.
