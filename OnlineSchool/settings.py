

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

import environ
env = environ.Env()
environ.Env.read_env()

import dj_database_url

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Your secret key
SECRET_KEY = env("SECRET_KEY")

# SECRET_KEY = 'django-insecure-h&xy=h%qtrb_=2gz2n386#(=v__6(9ri&w_dm_5#ejdawwif3)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    'dj_rest_auth',
    'users',
    'courses',
    'service',
    'contact_us',
    'blog',
    'enrollments',
    'reviews',
    'rest_framework.authtoken',
    "corsheaders",
    'payments',
]
LOGIN_URL="http://127.0.0.1:5500/login.html"

AUTH_USER_MODEL = 'users.CustomUser'
SITE_URL = "http://127.0.0.1:8000"


# settings.py
SSLCommerz_STORE_ID = 'abins671fc56b7ee72'
SSLCommerz_STORE_PASS = 'abins671fc56b7ee72@ss'

CSRF_TRUSTED_ORIGINS = [
    # 'http://127.0.0.1:5501', 
    # 'http://127.0.0.1:8000', 
    # 'http://127.0.0.1:5500',
    # 'https://online-school-2ldr.onrender.com,'
    'https://onlineschool-im71.onrender.com',
    'http://*.127.0.0.1'
     
]

ALLOWED_HOSTS = ["127.0.0.1", ".vercel.app"]

# CORS_ALLOW_METHODS = (
#     "DELETE",
#     "GET",
#     "OPTIONS",
#     "PATCH",
#     "POST",
#     "PUT",
# )

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:5500',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:5501',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'allauth.account.middleware.AccountMiddleware',   
    
]




ROOT_URLCONF = 'OnlineSchool.urls'
import os
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'OnlineSchool.wsgi.app'

CORS_ALLOW_ALL_ORIGINS = True 

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres.vhcflhykswfbxtwbfsnr',
        'PASSWORD': 'QWD267#yciuJER8',
        'HOST': 'aws-0-ap-southeast-1.pooler.supabase.com',
        'PORT': '6543'
    }
}



# Data base 

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': env("DB_NAME"),
#         'USER': env("DB_USER"),
#         'PASSWORD': env("DB_PASSWORD"),
#         'HOST': env("DB_HOST"),
#         'PORT': env("DB_PORT"),
#     }
# }

# DATABASES = {
#     'default':dj_database_url.config(
#         default='postgresql://online_school_fvmk_user:2CQoYALe8Xfx2FSIuFIYHlyUb7wX7Kv2@dpg-cquechogph6c73a00b6g-a.oregon-postgres.render.com/online_school_fvmk',
#     )
# }



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated',
    ),
}



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
REST_AUTH = {
    'ACCOUNT_CONFIRM_EMAIL_ON_GET': True,
    'ACCOUNT_EMAIL_VERIFICATION': 'mandatory',
    'ACCOUNT_EMAIL_REQUIRED': True,
}

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True




STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = env("EMAIL")
EMAIL_HOST_PASSWORD = env("EMAIL_PASSWORD")

