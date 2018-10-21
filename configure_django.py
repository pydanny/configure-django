# -*- coding: utf-8 -*-

"""Main module."""

import os
import shlex

import django
from django.conf import settings as django_settings
from django.core.exceptions import ImproperlyConfigured
from django.core.management import call_command

from decouple import config
from dj_database_url import parse as db_url

__author__ = "Daniel Roy Greenfeld"
__email__ = "pydanny@gmail.com"
__version__ = "0.3.5"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# TODO I believe this can be removed
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")


def configure(settings=None, command=None, run_migrations=False):
    """
      settings is a dictionary of UPPERCASE Django settings.

      command is a string that represents a Django management command.
          Example:
              migrate
              makemigrations myapp
    """
    if settings is None:
        INSTALLED_APPS = config(
            "DJANGO_INSTALLED_APPS",
            cast=lambda v: [s.strip() for s in v.split(',')],
            default="django.contrib.auth,django.contrib.contenttypes,django.contrib.sites"
        )

        DATABASES = {
            "default": config(
                "DATABASE_URL",
                default=os.path.join(f"sqlite://{BASE_DIR}", "db.sqlite3"),
                cast=db_url,
            )
        }

        settings = dict(
            DATABASES=DATABASES,
            INSTALLED_APPS=INSTALLED_APPS,
            ROOT_URLCONF="",  # tests override urlconf, but it still needs to be defined
            MIDDLEWARE_CLASSES=(),
        )

    # Configure environment
    try:
        django_settings.configure(**settings)
        # # TODO I believe this can be removed
        # django.setup()
    except RuntimeError:
        pass

    if command is not None:
        call_command(*shlex.split(command))

    if command is None and run_migrations is True:
        call_command(*["migrate"])
