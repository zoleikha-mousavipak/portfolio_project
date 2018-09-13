"""
WSGI config for portfolio_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

# import os
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_project.settings")
#
# application = get_wsgi_application()


import os
from django.core.wsgi import get_wsgi_application

# sys.path.append('portfolio_project')
os.environ.setdefault("PYTHON_EGG_CACHE", "portfolio_project.egg_cache")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PROJECT.settings")

application = get_wsgi_application()
