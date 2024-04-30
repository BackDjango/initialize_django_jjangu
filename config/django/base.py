import environ, os
from config.env import APPS_DIR, BASE_DIR, env
from config.settings import *


# SECRET_KEY 생성 및 분리
environ.Env().read_env(os.path.join(BASE_DIR, '.env'))
SECRET_KEY = env('SECRET_KEY')

DEBUG = env.bool("DJANGO_DEBUG", default=True)
ALLOWED_HOSTS = [ "*" ]

# Applicaiton Definitions
LOCAL_APPS = []
THIRD_PARTY_APPS = []
INSTALLED_APPS = []
MIDDLEWARE = []
ROOT_URLCONF = []
TEMPLATES = []
WSGI_APPLICATION = ""


# Database
DATABASES = {}
AUTH_PASSWORD_VALIDATORS = []
AUTH_USER_MODEL = ""


# Internationalization
LANGUAGE_CODE = "ko-KR"
TIME_ZONE = "Asia/Seoul"
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static Files
STATIC_ROOT = None
STATIC_URL = None
STATICFILES_STORAGE = None
REST_FRAMEWORK = {}
APP_DOMAIN = None
DEFAULT_AUTO_FIELD = None