#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys

from setuptools import setup


def get_version(*file_paths):
    """Retrieves the version from pre_commit_absent_migrations/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


version = get_version("pre_commit_absent_migrations/__init__.py")


if sys.argv[-1] == "publish":
    try:
        import wheel

        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system("python setup.py sdist upload")
    os.system("python setup.py bdist_wheel upload")
    sys.exit()

if sys.argv[-1] == "tag":
    print("Tagging the version on git:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open("README.rst").read()
history = open("HISTORY.rst").read().replace(".. :changelog:", "")
requirements = open("requirements.txt").readlines()

setup(
    name="pre-commit-absent-migrations",
    version=version,
    description="""Pre-commit hook for absent migration""",
    long_description=readme + "\n\n" + history,
    author="FrankHood Business Solutions srl",
    author_email="info@frankhood.it",
    url="https://github.com/frankhood/pre-commit-hooks-django-migrations",
    packages=[
        "pre_commit_absent_migrations",
    ],
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords="hooks",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.11",
    ],
    entry_points={
        "console_scripts": [
            "check-migrations = pre_commit_absent_migrations.makemigrations_check_absent:makemigrations_check_absent",
        ],
    },
)
