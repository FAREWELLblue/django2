"""
Django settings for dadashop12 project.

Generated by 'django-admin startproject' using Django 1.11.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2-sk@e-xa42pmoh8!4ks1mpskwlpwot_b(4nad+jl-^t7kssr4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'user',
    'dtoken',
    'goods',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dadashop12.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dadashop12.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dadashop12',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# 用户上传上来的文件,成为Media files[媒体文件]
# 标识出 什么样的请求是访问有媒体文件的请求; 'http://127.0.0.1:8000/media/abc/a.jpg'-->代表当前请求想加载媒体文件
MEDIA_URL='/media/'
# 用户上传的媒体文件的存储目录;以及加载请求过来后,django去该目录下寻找资源
MEDIA_ROOT=os.path.join(BASE_DIR,'media')

PIC_URL='http://127.0.0.1:8000'+MEDIA_URL


# 跨域CORS
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)
CORS_ALLOW_HEADERS = (
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)

# jwt key
JWT_TOKEN_KEY='1234567'
# 方案1[详情见day07缓存相关方法]
# from django.core.cache import cache
# cache.set/get-->操作的是redis中字符串类型
# 方案2[]
# from django_redis import get_redis_connection
# r=get_redis_connection() 可建立连接,可以操作redis所有的数据结构

#   django_redis.compressors.zlib.ZlibCompressor

CACHES = {
    "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            }
        },
    "goods": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379/5",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
                'COMPRESSOR':'django_redis.compressors.zlib.ZlibCompressor',# 开启压缩
            }
        },
    "goods_detail": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379/6",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
                'COMPRESSOR':'django_redis.compressors.zlib.ZlibCompressor',# 开启压缩
            }
        },
}
APPEND_SLASH=False
# 邮箱配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # 固定写法 引擎
EMAIL_HOST = 'smtp.qq.com' # 腾讯QQ邮箱 SMTP 服务器地址
EMAIL_PORT = 25  # SMTP服务的端口号
EMAIL_HOST_USER = '956649931@qq.com'  # 发送邮件的QQ邮箱
EMAIL_HOST_PASSWORD = 'wehrcyyzcraibeie'  # 在QQ邮箱->设置->帐户->“POP3/IMAP......服务” 里得到的在第三方登录QQ邮箱授权码
ADMINS=[('name','邮箱'),()]#错误时给谁发邮件
SERVER_EMAIL='授权的邮箱'

#微博相关信息
WEIBO_CLIENT_ID='924520904'# id
WEIBO_CLIENT_SECRET='cc9520251d5a4821280ff6f3e4f5b39e'# secret
WEIBO_REDIRECT_URI='http://127.0.0.1:7000/dadashop/templates/callback.html'

