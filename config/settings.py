"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-#ybf_pw$-%59s=3^vlo_y8a)=mjb_!ibpawqq2_@a29f%_^28h"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "markdownify.apps.MarkdownifyConfig",
    "social_django",
    "mainapp",
    "authapp",
    "crispy_forms",
    "debug_toolbar",
    #    "django_admin_filters",
    "rangefilter",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.media",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "mainapp.context_processors.example.simple_context_processor",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "authapp.CustomUser"

AUTHENTICATION_BACKENDS = (
    "social_core.backends.github.GithubOAuth2",
    "social_core.backends.google.GoogleOAuth2",
    "social_core.backends.yandex.YandexOAuth2",
    "social_core.backends.steam.SteamOpenId",
    "django.contrib.auth.backends.ModelBackend",
)

# LOGIN_URL = '/auth/login/google-oauth2/'
LOGIN_REDIRECT_URL = "mainapp:main_page"
LOGOUT_REDIRECT_URL = "mainapp:main_page"

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Media files
MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"

SOCIAL_AUTH_GITHUB_KEY = "d9ff0510081096ab4656"
SOCIAL_AUTH_GITHUB_SECRET = "9401c1baf17c965a8152b6e197d2d0f4ba7ee243"

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "834073725128-7bprcq5kgc6ng64t5mukkigl9kssoqqh.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "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"

SOCIAL_AUTH_YANDEX_OAUTH2_KEY = "369158b26a5d4a91979927bf229794d0"
SOCIAL_AUTH_YANDEX_OAUTH2_SECRET = "984492ce736c43b48328f90b622e4a42"

SOCIAL_AUTH_STEAM_API_KEY = "A709414B778D319627C5ED922AC112E9"
SOCIAL_AUTH_STEAM_EXTRA_DATA = ["username"]

# SOCIAL_AUTH_URL_NAMESPACE = 'social'

CRISPY_TEMPLATE_PACK = "bootstrap4"

LOG_FILE = BASE_DIR / "var" / "log" / "main_log.log"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {"format": "[%(asctime)s] %(levelname)s %(name)s (%(lineno)d) %(message)s"},
    },
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": LOG_FILE,
            "formatter": "console",
        },
        "console": {"class": "logging.StreamHandler", "formatter": "console"},
    },
    "loggers": {
        "django": {"level": "INFO", "handlers": ["console"]},
        "mainapp": {
            "level": "DEBUG",
            "handlers": ["file"],
        },
    },
}

# Redis
ALLOWED_HOSTS = ["*"]
# Redis
if DEBUG:
    INTERNAL_IPS = [
        "192.168.42.139",
        "192.168.42.1",
        "127.0.0.1",
    ]


# Redis In the end of file
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

# Celery
CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"


# Full list of email settings:
#   https://docs.djangoproject.com/en/3.2/ref/settings/#email
EMAIL_HOST = "smtp.yandex.ru"
EMAIL_PORT = "465"

# For debugging: python -m smtpd -n -c DebuggingServer localhost:25
EMAIL_HOST_USER = "levonAS0@yandex.ru"
EMAIL_HOST_PASSWORD = "XXXXXX"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# Email as files for debug
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = "var/email-messages/"

LOCALE_PATHS = [BASE_DIR / "locale"]
