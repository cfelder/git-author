git-author
==========

.. image:: https://img.shields.io/pypi/v/git-author.svg
    :target: https://pypi.python.org/pypi/git-author
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/l/git-author.svg
    :target: https://pypi.python.org/pypi/git-author
    :alt: License

| git-author, a git command for managing multiple authors.


Home Page
---------

Project home page is https://github.com/cfelder/git-author


Usage
-----

Configure multiple users, e.g.::

    git config --global gitauthor.guest.name "Guest User"
    git config --global gitauthor.guest.email "guest.user@example.com"

    git config --global gitauthor.john.name "John Doe"
    git config --global gitauthor.john.email "john.doe@example.com"

Get a list of configured users::

    $ git-author

    The following authors have been configured:

               guest:  Guest User <guest.user@example.com>
                john:  John Doe <john.doe@example.com>

             default:  Christian Felder <webmaster@bsm-felder.de>

Select specific user::

    git-author john

Finally commit your changes as usual in this session using::

    git commit


License
-------

The git-author library is open source software released under the
**LGPL-3.0+ license** (http://www.gnu.org/licenses/lgpl-3.0.html).


PEP8 Compliance
---------------

git-author is PEP8 compliant.


Download
--------

Package download is available at https://pypi.python.org/pypi/git-author.


Install
-------

git-author can be installed from the Python Package Index using ``pip`` or
``pip3``. ::

   $ pip3 install git-author

As ``git-author`` needs to change environment variables in your shell, it is
necessary to source the git-author script. Please add an alias pointing to
the ``git-author`` script to your environment, e.g.::

    alias git-author='source /usr/local/bin/git-author'


Git repository
--------------

You can download the latest source at https://github.com/cfelder/git-author

