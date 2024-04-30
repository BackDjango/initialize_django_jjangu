import environ, os
from config.env import APPS_DIR, BASE_DIR, env
from config.settings import *


# SECRET_KEY 생성 및 분리
environ.Env().read_env(os.path.join(BASE_DIR, '.env'))
SECRET_KEY = env('SECRET_KEY')

DEBUG = env.bool("DJANGO_DEBUG", default=True)
ALLOWED_HOSTS = [ "*" ]

# Applicaiton Definitions
LOCAL_APPS = [
    
]
THIRD_PARTY_APPS = [
    "rest_framework",
    # "django_celery_results",
    # "django_celery_beat",
    # "django_filters",
    # "corsheaders",
    # "django_extensions",
    # "rest_framework_jwt",
]
# Combine all above things
INSTALLED_APPS = [
    # 'django.contrib.admin',
    # 'django.contrib.auth',
    # 'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    # 'django.contrib.messages',
    *THIRD_PARTY_APPS,
    *LOCAL_APPS,
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # "corsheaders.middleware.CorsMiddleware",
    # "whitenoise.middleware.WhiteNoiseMiddleware",
    # "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware",
    # "django.contrib.auth.middleware.AuthenticationMiddleware",
    # "django.contrib.messages.middleware.MessageMiddleware",
    # "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
ROOT_URLCONF = "config.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(APPS_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                # "django.contrib.auth.context_processors.auth",
                # "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
WSGI_APPLICATION = "config.wsgi.application"


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