"""Tests for `configure_django` package."""

import os
import unittest

from configure_django import configure


class TestConfigure_django(unittest.TestCase):
    """Tests for `configure_django` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        configure()

    def test_settings_installed_apps(self):
        """Test if settings are configured."""
        from django.conf import settings

        self.assertListEqual(
            settings.INSTALLED_APPS,
            [
                "django.contrib.auth",
                "django.contrib.contenttypes",
                "django.contrib.sites",
            ],
        )

    def test_settings_databases(self):
        """Test if settings are configured."""
        from django.conf import settings

        del settings.DATABASES["default"]["NAME"]
        self.assertDictEqual(
            settings.DATABASES,
            {
                "default": {
                    "ATOMIC_REQUESTS": False,
                    "AUTOCOMMIT": True,
                    "CONN_MAX_AGE": 0,
                    "ENGINE": "django.db.backends.sqlite3",
                    "HOST": "",
                    "OPTIONS": {},
                    "PASSWORD": "",
                    "PORT": "",
                    "TEST": {
                        "CHARSET": None,
                        "COLLATION": None,
                        "MIRROR": None,
                        "NAME": None,
                    },
                    "TIME_ZONE": None,
                    "USER": "",
                }
            },
        )
