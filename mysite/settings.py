import os
from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api
import dj_database_url
from urllib.parse import urlparse
from django.contrib.messages import constants as messages

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-pky33&-@65dl3@+tf$f^%6n=+d+soh$#dx&3tps67ccgjlt1!m",
)
DEBUG = True
ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = [
    "https://web-production-7bca.up.railway.app",
]

# APPLICATIONS
INSTALLED_APPS = [
    # Core Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",

    # Your old apps
    "admin_soft.apps.AdminSoftDashboardConfig",
    "accounts",
    "core",
    "transactions",
    "bankcard",

    # Third-party
    "corsheaders",
    "storages",
]

# MIDDLEWARE
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "mysite.urls"
AUTH_USER_MODEL = "accounts.User"
LOGIN_URL = "/accounts/login/"

# TEMPLATES
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "mysite.wsgi.application"

# DATABASE
DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql://neondb_owner:npg_tYn2GTgKpez4@ep-lingering-haze-ad2ktmuu-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require",
)

DATABASES = {
    "default": dj_database_url.config(
        default=DATABASE_URL,
        conn_max_age=600,
        ssl_require=True,
    )
}


# PASSWORDS
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {"min_length": 4},
    },
]

# INTERNATIONALIZATION
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# STATIC & MEDIA
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# MESSAGES
MESSAGE_TAGS = {
    messages.SUCCESS: "alert-success",
    messages.ERROR: "alert-danger",
}

# AUTH BACKENDS
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "accounts.backends.AccountNoBackend",
    "accounts.backends.CustomAuthBackend",
)

# CLOUDINARY
cloudinary.config(
    cloud_name="demge4dml",
    api_key="376652426716721",
    api_secret="QVEXq4aB8IvMJTR6SbEAZJQJPIk",
)
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

# EMAIL
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.zoho.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "support@-"
EMAIL_HOST_PASSWORD = "Support51a511$$"
DEFAULT_FROM_EMAIL = "support@-"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
