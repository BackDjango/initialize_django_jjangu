"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# config.settings 폴더를 통해 asgi 서버 설정을 모듈화
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.django.base')

application = get_asgi_application()
