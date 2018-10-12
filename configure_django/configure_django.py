# -*- coding: utf-8 -*-

"""Main module."""

import os

import django
from django.conf import settings as django_settings
from django.core.exceptions import ImproperlyConfigured
from django.core.management import call_command

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
        try:
            INSTALLED_APPS = os.environ['DJANGO_INSTALLED_APPS'].split(',')
        except KeyError:
            raise ImproperlyConfigured("DJANGO_INSTALLED_APPS must be set.")

        settings = dict(
            DATABASES={
                "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}
            },
            INSTALLED_APPS=INSTALLED_APPS,
            ROOT_URLCONF="",  # tests override urlconf, but it still needs to be defined
            MIDDLEWARE_CLASSES=()
        )

    # Configure environment
    try:
        django_settings.configure(**settings)
        # TODO I believe this can be removed
        django.setup()
    except RuntimeError:
        pass

    if command is not None:
        call_command(*command.split(' '))

    if command is None and run_migration is True:
        call_command(*['migrate', ])