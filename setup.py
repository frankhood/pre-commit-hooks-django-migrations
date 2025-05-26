#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

from setuptools import setup

def get_version(*file_paths):
    """Retrieves the version from hooks/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


version = get_version("hooks/__init__.py")

setup(
    version=version
)
