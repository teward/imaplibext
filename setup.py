from setuptools import find_packages, setup
from imaplibext import __version__ as version

setup(
    name='imaplibext',
    version=version,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'typing',
    ],
    author='Thomas Ward',
    author_email='teward@dark-net.io',
    description="An imaplib extension module, that provides versions of IMAP4 and IMAP4_SSL with UID-based functions.",
    long_description="This is an extension module for `imaplib`. The functions of 'copy', 'search', 'fetch', 'store', "
                     "and possibly others, in the standard `imaplib` module do not return unique-identifier message "
                     "numbers in their number sets, which makes interaction with messages via 'store' a little bit "
                     "more difficult, and can result in the wrong messages being adjusted. This extension module is "
                     "designed to override the 'copy', 'search', 'fetch', and 'store' functions and provide UID-based "
                     "commands, by using the `uid` command and passing UID-format commands for the functions that are "
                     "overridden.",
    license='AGPLv3+',
    url='https://github.com/teward/imaplibext',
    download_url='https://pypi.python.org/pypi/imaplibext',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Communications :: Email',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='imaplib imap UID email',
    platforms='any',
    test_suite='tests'
)
