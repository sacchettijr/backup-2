# Django 4.0.1
import os
from pathlib import Path
from django.contrib.messages import constants as messages_constants

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-0ozcdi__i-g-mhmf6$1ij!z&cximh#$c8po*^jad!2a*4+t5)&'
DEBUG = True
ROOT_URLCONF = 'setup.urls'
WSGI_APPLICATION = 'setup.wsgi.application'
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Manaus'
USE_I18N = True
USE_TZ = False
HTML_MINIFY = True
AUTH_USER_MODEL = 'usuario.Usuario'
LOGIN_REDIRECT_URL = 'publico_index'
LOGOUT_REDIRECT_URL = 'publico_index'

ALLOWED_HOSTS = [
	'127.0.0.1',
]

INSTALLED_APPS = [
	# DJANGO
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	# DJANGO REST FRAMEWORK
	'rest_framework',
	'rest_framework.authtoken',
	'django_filters',
	'guardian',
	# BIBLIOTECAS
	'widget_tweaks',
	# APP
	'publico',
	'geral',
	'usuario',
	'produto',
	'venda',
]

MIDDLEWARE = [
	'htmlmin.middleware.HtmlMinifyMiddleware',
	'htmlmin.middleware.MarkRequestMiddleware',
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': ['templates'],
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

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': BASE_DIR / 'db.sqlite3',
	}
}

AUTH_PASSWORD_VALIDATORS = [
	{'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
	{'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
	{'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
	{'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

REST_FRAMEWORK = {
	'DEFAULT_PERMISSION_CLASSES': [
		'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
	],
	'DEFAULT_AUTHENTICATION_CLASSES': [
		'rest_framework.authentication.BasicAuthentication',
		'rest_framework.authentication.SessionAuthentication',
	]
}

AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',  # default
	'guardian.backends.ObjectPermissionBackend',
)

MESSAGE_TAGS = {
	messages_constants.SUCCESS: 'success',
	messages_constants.WARNING: 'warning',
	messages_constants.ERROR: 'danger',
	messages_constants.INFO: 'info',
	messages_constants.DEBUG: 'debug',
}

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
