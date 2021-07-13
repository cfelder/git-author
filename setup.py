#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import os.path
from setuptools import find_packages, setup

import vcversioner

__author__ = "Christian Felder <webmaster@bsm-felder.de>"
__version__ = vcversioner.find_version(
    version_module_paths=[os.path.join("git_author",
                                       "_version.py")]).version
__copyright__ = """Copyright 2019-2021, Christian Felder

This file is part of git-author, a git command for managing multiple authors.

git-author is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

git-author is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with git-author. If not, see <http://www.gnu.org/licenses/>.

"""


with open("README.rst", 'r') as fd:
    long_description = fd.read()


def find_scripts(where="bin"):
    return [os.path.join(where, name) for name in os.listdir(where) if
            os.path.isfile(os.path.join(where, name))]


setup(name="git-author",
      version=__version__,
      description="git-author, a git command for managing multiple authors",
      long_description=long_description,
      author="Christian Felder",
      author_email="webmaster@bsm-felder.de",
      url="https://github.com/cfelder/git-author",
      license="LGPL-3.0+",
      scripts=find_scripts(),
      packages=find_packages(exclude=["test", "test.*"]),
      include_package_data=True,
      install_requires=["git-review>=1.27.0"],
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: GNU General Public License v3 or later "
          "(GPLv3+)",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 3",
          "Topic :: Software Development",
          "Topic :: Software Development :: Version Control",
          "Topic :: Software Development :: Version Control :: Git"
      ],
     )
