import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR        = Path(__file__).resolve().parent.parent
SECRET_KEY      = os.getenv('SECRET_KEY')
DEBUG           = os.getenv('LOCAL_DEBUG') if 'LOCAL_DEBUG' in os.environ else os.getenv('PROD_DEBUG')

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mail.urls'

TEMPLATES = [
    {
        'BACKEND'   : 'django.template.backends.django.DjangoTemplates',
        'DIRS'      : [os.path.join(BASE_DIR, '../templates')],
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

WSGI_APPLICATION = 'mail.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Email Configurations ( Sendgrid Creds )
EMAIL_BACKEND       = os.getenv('EMAIL_BACKEND')
EMAIL_HOST          = os.getenv('EMAIL_HOST')
EMAIL_USE_TLS       = os.getenv('EMAIL_USE_TLS')
EMAIL_HOST_USER     = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT          = os.getenv('EMAIL_PORT')
DEFAULT_FROM_EMAIL  = os.getenv('DEFAULT_FROM_EMAIL')


# Email Configurations ( Mail GunCreds)
EMAIL_BACKEND_MAILGUN = os.getenv('EMAIL_BACKEND_MAILGUN')
MAILGUN_ACCESS_KEY    = os.getenv('MAILGUN_ACCESS_KEY')
MAILGUN_SERVER_NAME   = os.getenv('MAILGUN_SERVER_NAME')
MAILGUN_PORT          = os.getenv('MAILGUN_PORT')


#Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE   = 'en-us'
TIME_ZONE       = 'UTC'
USE_I18N        = True
USE_L10N        = True
USE_TZ          = True


# Logging setting
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format'    : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt'   : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format'    : '%(levelname)s %(message)s'
        },
    },
    'handlers'  : {
        'file'  : {
            'level'     : 'DEBUG',
            'class'     : 'logging.FileHandler',
            'formatter' : 'verbose',
            'filename'  : "logs/django-error.log",
        },
    },
    'loggers': {
        'django.request': {
            'handlers'  : ['file'],
            'level'     : 'DEBUG',
            'propagate' : True,
        },
        'api': {
            'handlers'  : ['file'],
            'level'     : 'DEBUG',
        }
    },
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
