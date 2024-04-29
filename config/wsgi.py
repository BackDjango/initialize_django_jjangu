"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# base.py 를 바탕으로 애플리케이션 서버 가져옴
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.django.base')

application = get_wsgi_application()
