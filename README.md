## IMAP Lib Extension Module

### Basic Information

<table>
<tr><td align=center valign=center><a href="http://www.gnu.org/licenses/agpl-3.0" target="_blank"><img src="https://img.shields.io/badge/License-AGPL%20v3-blue.svg" title="AGPL 3.0" /></a></td></tr>
<tr><td align=center valign=center><a href="https://pypi.python.org/pypi/imaplibext" target="_blank"><img src="http://img.shields.io/pypi/v/imaplibext.svg" title="PyPI Version" /></a></td></tr>
</table>


### Continuous Integration Status

| CI Provider           | Status                                                                                                                                      |
|:---------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------:|
| GitLab CI             | [![Pipeline Status](https://gitlab.com/teward/imaplibext/badges/master/pipeline.svg)](https://gitlab.com/teward/imaplibext/commits/master)  |
| Appveyor              | [![Build status](https://ci.appveyor.com/api/projects/status/qtpyo61gxt7x2s5q?svg=true)](https://ci.appveyor.com/project/teward/imaplibext) |

<!--| CircleCI (via GitHub) | [![CircleCI](https://circleci.com/gh/teward/pytio.svg?style=svg)](https://circleci.com/gh/teward/pytio)                                     |
| TravisCI (via GitHub) | [![Build Status](https://travis-ci.org/teward/pytio.svg?branch=master)](https://travis-ci.org/teward/pytio)                                 |-->

## Description

This module is designed to use the existing `imaplib` library functionality, but extends upon it.

When using standard `imaplib` functions such as 'search' or 'fetch', the `imaplib` libraries do not use UID numbers in 
the returned `messageset`, which means that augmenting flags via the 'store' function or similar can sometimes modify 
the wrong message in the inbox, as the numbers returned by the default functions in `imaplib` do not correspond to the 
UID (Unique ID) of the individual messages.

This extension library, `imaplibext`, is a very simple set of classes (`IMAP4` and `IMAP4_SSL`) that inherit from the 
parent class of the same name in `imaplib`, but redefines the following functions to use the `uid` command instead of 
the built-in commands usually called by these functions.  In this manner, we get UID-based message numbers in the 
message-sets being returned or handled, and are able to more properly handle messages uniquely without collissions.

This was inspired as a result of [a question initially asked by the author of this module on StackOverflow][1], in 
which the author needed to be able to manipulate the "Seen" flag on messages properly in one of their scripts via a 
Python program.  While the author of this module found multiple solutions, either by changing the 'fetch' command call 
in the script they used, or by replacing the default 'search', 'fetch', 'store' functions with `.uid` functions instead,
this made understanding the code hard by his co-workers.  To adjust for this, he created this module which provides
UID-based forms of the commands, which use UID references instead of non-UID message numbers.


## Compatibility

This module was written to be Python 2 and Python 3 compatible.  It should work properly with both Python 2 and Python 3
and uses the Python 2 type hinting suggested in [PEP 484][2], but also the `typing` module that is now in `pip`


## Installation / Usage

### Use PyPI

This library is available from the PyPI repository.

#### Python 2:


### Install from Source Code

#### Dependencies

First, install the dependencies from PyPI.

##### Python 2

For system-wide installation:

    pip install --upgrade -r requirements.txt
    
For user-space installation:

    pip install --user --upgrade -r requirements.txt
    
##### Python 3

For system-wide installation:

    pip3 install --upgrade -r requirements.txt

For user-space installation:

    pip3 install --user --upgrade -r requirements.txt

### Installing / Importing in Code

Simply copy the `imaplibext` package folder into your working directory for your Python script or program.

## Usage

Once installed in either method, you can import into your Python code as a drop-in replacement for `imaplib`'s 
`IMAP4` or `IMAP4_SSL` commands.

    # Use this to import as a module and call things with `imaplibext.OBJECTNAME`
    import imaplibext
    
    # or, use this, to call IMAP4 and IMAP4_SSL directly in your code, but get the UID functions instead.
    from imaplibext import IMAP4, IMAP4_SSL
    
## Usage

Usage is identical to `imaplib`'s `IMAP4` and `IMAP4_SSL` classes and corresponding function calls. There is no real
difference in how to reference functions or the classes in the IMAP4 or IMAP4_SSL functions here compared to the parent
`imaplib` functions.


## FAQ

### Where can I report issues or make Feature Requests?

Issues and feature requests can be reported on the [Gitlab Repository](https://gitlab.com/teward/imaplibext)


[1]: https://stackoverflow.com/questions/42631422/mark-a-single-imap-message-as-unread
[2]: https://www.python.org/dev/peps/pep-0484/#suggested-syntax-for-python-2-7-and-straddling-code
[3]: https://youtrack.dark-net.io/newissue?project=IMAP_PY
