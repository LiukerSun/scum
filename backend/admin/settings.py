import os
import configparser
from corsheaders.defaults import default_headers

# Read conf from file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
conf = configparser.RawConfigParser()
conf.read(BASE_DIR + "/config.ini", encoding="utf-8")
JWT_TOKEN = conf.get("jwt", "token")
DEBUG = conf.get("global", "Debug")
SECRET_KEY = conf.get("global", "SecretKey")

# CORS SETTING
CORS_ALLOW_HEADERS = default_headers + ("access-control-allow-origin",)
ALLOWED_HOSTS = ["*"]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_EXPOSE_HEADERS = ["Content-Disposition"]
CORS_ORIGIN_WHITELIST = ("http://127.0.0.1:8000",)

# APP
INSTALLED_APPS = [
    "django.contrib.postgres",
    "drf_yasg",
    "rest_framework",
    "channels",
    "auth",
    "device",
]

# MIDDLEWARE
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",  # or use RedisChannelLayer for production
    },
}

CACHES = {
    "devices": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",  # 这里的 1 是数据库的编号
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "commands": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",  # 这里的 2 是数据库的编号
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}


# URL
ROOT_URLCONF = "admin.urls"

# LOG
DJANGO_LOG_LEVEL = "DEBUG"

# WSGI_APPLICATION = "admin.wsgi.application"
ASGI_APPLICATION = "admin.asgi.application"

REST_FRAMEWORK = {
    "UNAUTHENTICATED_USER": None,
}
# DB
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": conf.get("db", "DataBase"),
        "USER": conf.get("db", "User"),
        "PASSWORD": conf.get("db", "Password", raw=True),
        "HOST": conf.get("db", "Host"),
        "PORT": conf.get("db", "Port"),
    }
}
