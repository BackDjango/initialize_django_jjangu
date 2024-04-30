import environ, os
from config.env import APPS_DIR, BASE_DIR, env

# SECRET_KEY 생성 및 분리
env = environ.Env()
environ.Env().read_env(os.path.join(BASE_DIR, '.env'))
SECRET_KEY = env('SECRET_KEY')


DEBUG = True

LOCAL_APPS = []

THIRD_PARTY_APPS = []

INSTALLED_APPS = []

MIDDLEWARE = []

ROOT_URLCONF = []

TEMPLATES = []

WSGI_APPLICATION = ""

DATABASES = {}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = "ko-KR"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_ROOT = None
STATIC_URL = None
STATICFILES_STORAGE = None

REST_FRAMEWORK = {}

APP_DOMAIN = None

DEFAULT_AUTO_FIELD = None