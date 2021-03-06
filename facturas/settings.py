"""
Django settings for facturas project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g$gn*l1g+s&&b8awxk@hgr6%4w(-vk9n#_u8%b29_l%p_9jt#4'

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
    # my apps
    'accounts',
    'products',
    'customers',
    'dashboard',
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

ROOT_URLCONF = 'facturas.urls'

# Lin,Leo - by default, django loads every template from
# the 'template' folder within every app from 'DIRS'.
# To override this behavior and create a template at
# our django project level, it uses 'APP_DIRS'.

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # Lin,Leo - here we place all our templates
                                                       # under django-project/templates folder.
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

WSGI_APPLICATION = 'facturas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

## STATIC_URL is is the URL of which the static files stored in
## STATIC_ROOT path  are served (Apache or nginx).
## Example: /static/ or http://static.example.com/
##
## if you set 'STATIC_URL' = 'http://static.example.com', then you must
## serve the 'STATIC_ROOT' folder by apache or nginx at 'http://static.example.com/'.
## When used in the template
## <link rel="stylesheet" href="{{ STATIC_URL }}css/base.css" type="text/css"/>
## link is converted into
## <link rel="stylesheet" href="/static/css/base.css" type="text/css"/>
## and since href starts with /, final link will contain your domain
## <link ref="stylesheet" href="http://yourdomain/static/css/base/css" type=text/css"/>

STATIC_URL = '/static/'

# STATICFILES_DIR is used to include additional directories
# for 'collectstatic' to look for.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'proj_static_files')
]

## STATIC_ROOT is useless during development, it is only required for deployment
## When Debug=True, Django looks for static files inside each app's directory
## and severs them automatically.
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn", "static_root")

# redirect to this URL upon successfully logged-in
LOGIN_REDIRECT_URL = 'home' # this is the name given to our home url, see urls.py

# tells django.auth app to redirect to this url
# upon logging out!
LOGOUT_REDIRECT_URL = 'home' # this is the name given to our home url, see urls.py
