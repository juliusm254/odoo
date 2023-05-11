from .base import *  # noqa
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="LdUVZ1N8S7JUdDwlS8BAEPcBYcrTUqy94wV9x6eOq8vXwQpD0uqMQgpy0ZEk6EAa",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["127.0.0.1"]


# CORS_ORIGIN_ALLOW_ALL = True


# ALLOWED_HOSTS = [
#    "0.0.0.0:8000",
#    "127.0.0.1",
#    "agolfront-bvtwuypbsq-uc.a.run.app",
#    "agol-bvtwuypbsq-km.a.run.app",
#    "https://agolfront-bvtwuypbsq-uc.a.run.app/",
#    "https://agol-bvtwuypbsq-km.a.run.app",

# ]
CORS_ALLOWED_ORIGINS = [ "http://localhost:5173", "http://localhost:5174","http://127.0.0.1:5173","http://127.0.0.1:5174" ]
# CORS_ALLOWED_ORIGINS = [
#     "http://0.0.0.0:8000",
#     "http://172.18.0.2:8080",
#     "http://172.18.0.2",
#     "https://agolfront-bvtwuypbsq-uc.a.run.app",
#     "https://agolfront-bvtwuypbsq-uc.a.run.app:8080",
#     "https://agolfront-bvtwuypbsq-uc.a.run.app:80",
#     "https://agol-bvtwuypbsq-km.a.run.app",
#     "http://127.0.0.1",
#     "http://localhost",
#     "http://127.0.0.1:80",
#     "http://localhost:8080",]



# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)

# WhiteNoise
# ------------------------------------------------------------------------------
# http://whitenoise.evans.io/en/latest/django.html#using-whitenoise-in-development
INSTALLED_APPS = ["whitenoise.runserver_nostatic"] + INSTALLED_APPS  # noqa F405


# django-debug-toolbar
# ------------------------------------------------------------------------------
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
INSTALLED_APPS += ["debug_toolbar"]  # noqa F405
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa F405
# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
if env("USE_DOCKER") == "yes":
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]

# django-extensions
# ------------------------------------------------------------------------------
# https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#configuration
INSTALLED_APPS += ["django_extensions"]  # noqa F405

# Your stuff...
# ------------------------------------------------------------------------------
INSTALLED_APPS += ["faker"]

<<<<<<< Updated upstream
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=365),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=365),
    }
=======
# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(days=365),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=365),
#     }
>>>>>>> Stashed changes

