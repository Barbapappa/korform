"""
Django settings for korform project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qpmo9b^o0f^b1b=bqb!yx!3p_x0@p2vw-%hf!3#5gfq)ctf_1l'

# Site ID (leave it alone unless you're running multitenant sites)
SITE_ID = 1

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'registration',
    'crispy_forms',
    'djangobower',
    'pipeline',
    'markdown_deux',
    'korform_accounts',
    'korform_sites',
    'korform_planning',
    'debug_toolbar',
)

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
    'pipeline.finders.PipelineFinder',
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

ROOT_URLCONF = 'korform.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'korform.wsgi.application'

AUTH_USER_MODEL = 'korform_accounts.User'


# Assets
# https://django-bower.readthedocs.org/en/latest/
# https://django-pipeline.readthedocs.org/en/latest/

BOWER_COMPONENTS_ROOT = BASE_DIR

BOWER_INSTALLED_APPS = (
    'jquery',
    'bootstrap#~3.0',
)

PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
)

PIPELINE_CSS = {
    'app': {
        'source_filenames': (
            'bootstrap/dist/css/bootstrap.css',
            'css/app.less',
        ),
        'output_filename': 'css/style.css',
    },
}

PIPELINE_JS = {
    'app': {
        'source_filenames': (
            'jquery/dist/jquery.js',
            'bootstrap/dist/js/bootstrap.js',
            'js/app.js',
        ),
        'output_filename': 'js/script.js',
    },
}

PIPELINE_LESS_ARGUMENTS = '--include-path={bower}:{bower}/bootstrap/less'.format(
  bower=os.path.join(BASE_DIR, 'bower_components')
)


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'korform',
        'USER': 'korform',
        'PASSWORD': 'korform',
        'HOST': '127.0.0.1',
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
}



# Grappelli (admin UI)
# http://django-grappelli.readthedocs.org/en/latest/

GRAPPELLI_ADMIN_TITLE = u"Admin"



# Email
# https://docs.djangoproject.com/en/1.8/topics/email/

# EMAIL_HOST = 'smtp.example.com'
# EMAIL_PORT = 465
# EMAIL_USE_SSL = True
# EMAIL_USE_TLS = False
# EMAIL_HOST_USER = 'myusername'
# EMAIL_HOST_PASSWORD = 'mypassword'

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'emails')



# Account registration
# https://django-registration-redux.readthedocs.org/en/latest/

LOGIN_REDIRECT_URL = 'index'

ACCOUNT_ACTIVATION_DAYS = 7

INCLUDE_REGISTER_URL = False



# Debug toolbar
# http://django-debug-toolbar.readthedocs.org/en/latest/

DEBUG_TOOLBAR_PATCH_SETTINGS = False
DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': None,
    'SHOW_COLLAPSED': True,
    'SHOW_TOOLBAR_CALLBACK': 'korform.settings.show_toolbar_callback',
}

def show_toolbar_callback(request):
    return not request.is_ajax() and DEBUG



# Crispy Forms
# http://django-crispy-forms.readthedocs.org/en/latest/

CRISPY_TEMPLATE_PACK = 'bootstrap3'

CRISPY_FAIL_SILENTLY = not DEBUG



# Markdown
# https://github.com/trentm/django-markdown-deux

MARKDOWN_DEUX_STYLES = {
    "default": {
        "extras": {
            "code-friendly": True,
        },
        "safe_mode": True,
    },
    "trusted": {
        "extras": {
            "code-friendly": True,
        },
        "safe_mode": False,
    }
}



# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'www', 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'bower_components'),
)
