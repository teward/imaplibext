=========================
IMAP Lib Extension Module
=========================

License: `GNU Affero GPL 3.0 <https://www.gnu.org/licenses/agpl-3.0.txt>`_ (or later)

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

Issues can be reported on the `Dark-Net.IO YouTrack instance against the "imaplibext (Python)" project
<https://youtrack.dark-net.io/newissue?project=IMAP_PY>`_ (via the guest account, unfortunately, as YouTrack tends
to get very very expensive in the long run for many users; you can click the above link to go right to the "Issue
Creation" page).  Issues will be tracked there, and only there, and you get a better idea of the state of issues
or feature requests that way as well.  While this does not permit you to subscribe to such issue notifications,
you can get an at-a-glance idea of the state of your issue, without having to read through comments.
