#!/usr/bin/env python3
# coding: utf-8

from __future__ import print_function

import sys
import argparse
import subprocess
from collections import namedtuple
# pylint: disable=protected-access
# pylint: disable=unused-import
# noinspection PyProtectedMember
from git_author._version import __version__, __revision__


__author__ = "Christian Felder <webmaster@bsm-felder.de>"
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


Author = namedtuple("Author", ["name", "email"])


def run_command(*args):
    return subprocess.check_output(args,
                                   stdin=subprocess.PIPE,
                                   universal_newlines=True)


def create_parser():
    parser = argparse.ArgumentParser(
        description="git-author",
    )
    parser.add_argument("name", nargs='?')

    return parser


def parse_args(argv):
    parser = create_parser()
    return parser.parse_args(argv[1:])


def get_authors():
    out = run_command("git", "config", "--list")
    authors = {}
    tmp = {}
    for entry in out.splitlines():
        fullkey, value = entry.split('=', 1)
        if fullkey.startswith("gitauthor."):
            target = fullkey.split('.')[1]
        elif fullkey.startswith("user."):
            target = "default"
        else:
            continue

        if target not in tmp:
            tmp[target] = dict()

        key = fullkey.rsplit('.', 1)[1]
        if key in ["name", "email"]:
            tmp[target][key] = value

        if "name" in tmp[target] and "email" in tmp[target]:
            authors[target] = Author(name=tmp[target]["name"],
                                     email=tmp[target]["email"])
    return authors


def print_author(author):
    # this function should just print bash evaluable content to stdout
    print("export GIT_AUTHOR_NAME='%s'" % author.name)
    print("export GIT_AUTHOR_EMAIL='%s'" % author.email)


def main(argv):
    ns = parse_args(argv)
    authors = get_authors()

    if ns.name:
        if ns.name not in authors:
            print("No such author '%s'" % ns.name, file=sys.stderr)
            return -1
        print_author(authors[ns.name])
    elif authors:
        print("The following authors have been configured:")
        print()
        default_author = authors.pop("default", None)
        for target in sorted(authors):
            author = authors[target]
            print("%16s:  %s <%s>" % (target, author.name, author.email))

        if default_author:
            target = "default"
            print()
            print("%16s:  %s <%s>" % (target, default_author.name,
                                      default_author.email))


if __name__ == "__main__":
    main(sys.argv)
