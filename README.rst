=========================
IMAP Lib Extension Module
=========================

License: `GNU Affero GPL 3.0 <https://www.gnu.org/licenses/agpl-3.0.txt>`_ (or later)

**NOTICE! The GitHub repository is simply a mirror of the GitLab
repository. All development now takes place on GitLab. Please do not
open issues here on GitHub, they will get no attention at all and not be
addressed.**

Basic Information
-----------------
.. raw:: html

    <table>
    <tr><td align=center valign=center><a href="http://www.gnu.org/licenses/agpl-3.0" target="_blank"><img src="https://img.shields.io/badge/License-AGPL%20v3-blue.svg" title="AGPL 3.0" /></a></td></tr>
    <tr><td align=center valign=center><a href="https://pypi.python.org/pypi/imaplibext" target="_blank"><img src="http://img.shields.io/pypi/v/imaplibext.svg" title="PyPI Version" /></a></td></tr>
    </table>

Continuous Integration Status
-----------------------------

.. raw:: html

    <table>
    <tr><th align=center valign=center>CI Provider</th><th align=center valign=center>Status</th></tr>
    <tr><td align=center valign=center>GitLab CI</td><td align=center valign=center><a href="https://gitlab.com/teward/imaplibext/commits/master"><img alt="pipeline status" src="https://gitlab.com/teward/imaplibext/badges/master/pipeline.svg" /></a></td>
    <tr><td align=center valign=center>AppVeyor</td><td align=center valign=center><a href="https://ci.appveyor.com/project/teward/imaplibext"><img alt="AppVeyor CI" src="https://ci.appveyor.com/api/projects/status/qtpyo61gxt7x2s5q?svg=true" /></a></td></tr>
    <tr><td align=center valign=center>CircleCI (via GitHub)</td><td align=center valign=center><a href="https://circleci.com/gh/teward/imaplibext"><img alt="CircleCI" src="https://circleci.com/gh/teward/imaplibext.svg?style=svg" /></a></td></tr>
    <tr><td align=center valign=center>TravisCI (via GitHub)</td><td align=center valign=center><a href="https://travis-ci.org/teward/imaplibext"><img alt="Travis CI" src="https://travis-ci.org/teward/imaplibext.svg?branch=master" /></a></td></tr>
    </table>


Description
-----------

This module is designed to use the existing ``imaplib`` library functionality, but extends upon it.

When using standard ``imaplib`` functions such as 'search' or 'fetch', the ``imaplib`` libraries do not use UID
numbers the returned ``messageset``, which means that augmenting flags via the 'store' function or similar can
sometimes modify the wrong message in the inbox, as the numbers returned by the default functions in ``imaplib``
do not correspond to the UID (Unique ID) of the individual messages.

This extension library, ``imaplibext``, is a very simple set of classes (``IMAP4`` and ``IMAP4_SSL``) that inherit
from the parent class of the same name in ``imaplib``, but redefines the following functions to use the ``uid``
command instead of the built-in commands usually called by these functions.  In this manner, we get UID-based message
numbers in the message-sets being returned or handled, and are able to more properly handle messages uniquely without
collissions.

This was inspired as a result of `a question initially asked by the author of this module on StackOverflow
<https://stackoverflow.com/questions/42631422/mark-a-single-imap-message-as-unread>`_, in which the author needed to be
able to manipulate the "Seen" flag on messages properly in one of their scripts via a Python program.  While the author
of this module found multiple solutions, either by changing the 'fetch' command call in the script they used, or by
replacing the default 'search', 'fetch', 'store' functions with ``.uid`` functions instead, this made understanding the
code hard by his co-workers.  To adjust for this, he created this module which provides UID-based forms of the
commands, which use UID references instead of non-UID message numbers.

------

Compatibility
-------------

This module was written to be Python 2 and Python 3 compatible.  It should work properly with both Python 2 and
Python 3. and uses the Python 2 type hinting suggested in `PEP 484
<https://www.python.org/dev/peps/pep-0484/#suggested-syntax-for-python-2-7-and-straddling-code>`_, but also the
``typing`` module that is now in the PyPI repositories.

------

Installation / Usage
--------------------

**PyPI Repository**

Install with the following command:

::

    pip install imaplibext

------

If you are not using the PyPI repository, then follow the steps below.  Otherwise, just install ``imaplibext`` with
PyPI.

**Dependencies**

First, install the dependencies from PyPI.

*Python 2*

For system-wide installation:

::

    pip install --upgrade -r requirements.txt

For user-space installation:

::

    pip install --user --upgrade -r requirements.txt

*Python 3*

For system-wide installation:

::

    pip3 install --upgrade -r requirements.txt

For user-space installation:

::

    pip3 install --user --upgrade -r requirements.txt

**Installing / Importing in Code**

Simply copy the ``imaplibext`` package folder into your working directory for your Python script or program.

From there, you can import into your Python code as a drop-in replacement for ``imaplib``'s ``IMAP4`` or ``IMAP4_SSL``
commands.

::

    # Use this to import as a module and call things with `imaplibext.OBJECTNAME`
    import imaplibext

    # or, use this, to call IMAP4 and IMAP4_SSL directly in your code, but get the UID functions instead.
    from imaplibext import IMAP4, IMAP4_SSL

**Usage**

Usage is identical to ``imaplib``'s ``IMAP4`` and ``IMAP4_SSL`` classes and corresponding function calls. There is
no real difference in how to reference functions or the classes in the ``IMAP4`` or ``IMAP4_SSL`` functions here
compared to the parent ``imaplib`` functions.


Frequently Asked Questions
--------------------------

### Where can I report issues or make Feature Requests?

Issues and feature requests can be reported on the `Gitlab Repository <https://gitlab.com/teward/imaplibext>`_
