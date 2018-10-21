#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import sys, os
from setuptools import setup

version = "0.3.6"

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.md") as history_file:
    history = history_file.read()

if sys.argv[-1] == "publish":
    os.system("rm -rf dist")
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

requirements = ["dj-database-url", "python-decouple", 'django']

setup_requirements = []

test_requirements = []

setup(
    author="Daniel Roy Greenfeld",
    author_email="pydanny@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Framework :: Django",
        "Framework :: Django :: 2.1",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="A package for configuring Django in non-traditional environments.",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="configure_django",
    name="configure_django",
    py_modules=["configure_django"],
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/pydanny/configure_django",
    version=version,
    zip_safe=False,
)
