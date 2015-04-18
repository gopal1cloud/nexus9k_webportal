Nexus9k Community
=================
Community website for the Cisco Nexus 9000 series network switches.

See the `Contributing Guidelines`_ to get started.

Installation
------------
#. Install Python and create/activate a virtual environment:

   **Windows**

   #. Install the latest stable version of `Python for Windows`_.
   #. Create a virtual environment::

      $ cd c:/users/{username}
      $ mkdir .venvs
      $ cd .venvs
      $ c:/python{python version}/python -m venv nexus9k
      $ cd nexus9k/scripts
      $ activate

   **Unix**

   #. Install `python dependencies`_ needed to build Python from source.
   #. Install `pyenv <https://github.com/yyuu/pyenv-installer>`_ and follow
      instructions to build the *latest version* of Python.
   #. Install `pyenv virtualenv`_ and follow the instructions to create/activate
      virtual environment.

   .. _python for windows: https://www.python.org/downloads/windows/
   .. _python dependencies: https://github.com/yyuu/pyenv/wiki/Common-build-problems#requirements
   .. _pyenv virtualenv: https://github.com/yyuu/pyenv-virtualenv

#. Install dependencies:

   **Windows**

   #. Install `Git`_ if not already installed (for msysgit unix commands).
   #. Download `make`_.
   #. Copy make file to :code:`c:/program files (x86)/git/bin`.
   #. Add the bin to environment variables.

   **Unix**
   ::

    $ cd ~/home/nexus9k
    $ make install

   .. _git: http://git-scm.com/
   .. _make: http://repo.or.cz/w/msysgit.git?a=blob;f=bin/make.exe;h=a971ea1266ff40e89137bba068e2c944a382725f;hb=968336eddac1874c56cd934d10783566af5a3e26

#. Compile SCSS::

   $ make compile-scss

#. Watch SCSS files for changes to compile (only for developers)::

   $ make watch-scss

#. Run the server locally::

   $ make run-local


Development Server
------------------
**Note:** Commits pushed to this Github repository are automatically deployed
to the development server with `dploy io`_.

====== =======================
IP     104.236.133.94:8000
OS     Debian 7.0 (x64)
Server nginx + uwsgi
Env    pyenv (Python 3.4.3)
====== =======================

Start development server::

  $ pyenv activate nexus9k
  $ cd ~/home/nexus9k
  $ make run-public

.. _contributing guidelines: CONTRIBUTING.rst
.. _dploy io: http://dploy.io/


Browser Support
---------------
===========  ===========
Development  Chrome
Production   Full, > IE7
===========  ===========