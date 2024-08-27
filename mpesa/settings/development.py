from . base import *

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# import logging
# import logging.config

# from django.utils.log import DEFAULT_LOGGING

# logger = logging.getLogger(__name__)

# LOG_LEVEL = "INFO"

# logging.config.dictConfig(
#     {
#         "version": 1,
#         "disable_existing_loggers": False,
#         "formatters": {
#             "console": {
#                 "format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
#             },
#             "file": {"format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"},
#             "django.server": DEFAULT_LOGGING["formatters"]["django.server"],
#         },
#         "handlers": {
#             "console": {
#                 "class": "logging.StreamHandler",
#                 "formatter": "console",
#             },
#             "file": {
#                 "level": "INFO",
#                 "class": "logging.FileHandler",
#                 "formatter": "file",
#                 "filename": "logs/mpesa.log",
#             },
#             "django.server": DEFAULT_LOGGING["handlers"]["django.server"],
#         },
#         "loggers": {
#             "": {"level": "INFO", "handlers": ["console", "file"], "propagate": False},
#             "apps": {"level": "INFO", "handlers": ["console"], "propagate": False},
#             "django.server": DEFAULT_LOGGING["loggers"]["django.server"],
#         },
#     }
# )


