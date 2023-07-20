"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from os.path import abspath, dirname, join
from datetime import timedelta
import sys

from settings_params import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.

# BASE_DIR: 프로젝트의 최상위 경로를 뜻함
# BASE_DIR = Path(__file__).resolve().parent.parent (기존의 BASE_DIR)
BASE_DIR = dirname(dirname(dirname(abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    # Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    # Third Apps
    'rest_framework', # pip install djangorestframework
    'corsheaders', # pip install django-cors-headers: CORS 오류 방지
    'rest_framework.authtoken',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'django_pydenticon', # pip install django-pydenticon
    
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'requests', # pip install requests
    
    # S3 Storage
    'storages',
    
    # Locals Apps: 생성한 app list
    "accounts",
    "posts",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'corsheaders.middleware.CorsMiddleware', # CORS 관련 추가
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [f'{BASE_DIR}/templates'],
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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# sqlite3
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, "db.sqlite3"),
#     }
# }


DATABASES = DATABASES

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ko-kr'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

# USE_TZ = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


# Basic static1
STATIC_URL= 'static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')

# Basic static2
# STATIC_URL = 'static/'
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# default AUTH_USER 
AUTH_USER_MODEL = 'accounts.User'

# Custom Adapter
ACCOUNT_ADAPTER = 'accounts.adapters.CustomAccountAdapter'


# dj-rest-auth
REST_AUTH = {
    'USER_DETAILS_SERIALIZER': 'dj_rest_auth.serializers.UserDetailsSerializer',
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'my-app-auth',
    'JWT_AUTH_REFRESH_COOKIE': 'my-refresh-token',
    'JWT_AUTH_HTTPONLY' : False,
    'REGISTER_SERIALIZER': 'accounts.serializers.CustomRegisterSerializer', # Custom Serializer 
    'USER_DETAILS_SERIALIZER' : 'accounts.serializers.CustomUserDetailsSerializer', # Custom Serializer
}

SITE_ID = 1
ACCOUNT_USER_MODEL_USERNAME_FIELD = None # username 필드 사용 x
ACCOUNT_EMAIL_REQUIRED = True            # email 필드 사용 o
ACCOUNT_USERNAME_REQUIRED = False        # username 필드 사용 x
ACCOUNT_AUTHENTICATION_METHOD = 'email'

ACCOUNT_EMAIL_VERIFICATION = 'none' # 회원가입 과정에서 이메일 인증 사용 X
OLD_PASSWORD_FIELD_ENABLED = True # 비밀번호 변경 시 예전 비밀번호 입력


# REST_FRAMEWORK settings:
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.IsAdminUser',
    ],
     'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        # dj_rest_auth의 인증절차 중 JWTCookieAuthentication을 사용
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
     ]
}

# JWT 사용을 위한 설정
REST_USE_JWT = True


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=180), 
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False, # True일 경우: TokenRefeshView 에 retresh token을 보내면 새로운 access/refresh token 발급
    'BLACKLIST_AFTER_ROTATION': False, # True 일 시: 새로 고침 토큰 이 블랙리스트에 추가
    'UPDATE_LAST_LOGIN': False, # True 일 시: User 테이블의 last_login 필드가 로그인 시 업데이트

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None, # host site의 도메인
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION', # HTTP_  뒤 부분이 token 헤더 이름이 됨
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

AWS = False
if AWS:
    # AWS
    AWS_ACCESS_KEY_ID = AWS_ACCESS_KEY_ID # .csv 파일에 있는 내용을 입력 Access key ID
    AWS_SECRET_ACCESS_KEY = AWS_SECRET_ACCESS_KEY # .csv 파일에 있는 내용을 입력 Secret access key
    AWS_REGION = 'ap-northeast-2'

    # S3 Storages
    AWS_STORAGE_BUCKET_NAME = AWS_STORAGE_BUCKET_NAME # 설정한 버킷 이름
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (AWS_STORAGE_BUCKET_NAME,AWS_REGION)
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }

    # MEDIA
    MEDIA_URL = "https://%s/media/" % AWS_S3_CUSTOM_DOMAIN
    # DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    DEFAULT_FILE_STORAGE = 'settings_params.MediaStorage'
else:
    # MEDIA
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# password reset 시 이메일 전송 관련 설정
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'               # 메일을 호스트하는 서버
EMAIL_PORT = '587'                          # gmail과의 통신하는 포트
EMAIL_HOST_USER = EMAIL_HOST_USER           # 발신할 이메일
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD   # 발신할 메일의 비밀번호
EMAIL_USE_TLS = True                        # TLS 보안 방법
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER        # 사이트와 관련한 자동응답을 받을 이메일 주소


# pydenticon 관련 settings 내 Callable 참조가 3.9까지만 지원됨
# 몽키패칭으로 Callable 속성 복사
import collections
if not hasattr(collections, 'Callable'):
    collections.Callable = collections.abc.Callable