"""
<<<<<<< HEAD
WSGI config for web_site project.
=======
WSGI config for umafoto_ae project.
>>>>>>> 74158fa133f790eef2dbaacc7130963fa5c60e20

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_site.settings.dev")
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_site.settings')
>>>>>>> 74158fa133f790eef2dbaacc7130963fa5c60e20

application = get_wsgi_application()
