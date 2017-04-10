from setuptools import find_packages, setup


setup(
    name='imaplibext',
    version='0.2.1-alpha1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'typing',
    ],
    author='Thomas Ward',
    author_email='teward@dark-net.io',
    description="An imaplib extension module, that provides versions of IMAP4 and IMAP4_SSL which use functions (such "
                "as 'search', 'fetch', 'store') which return or use UID-based message-set identifiers to better handle "
                "messages uniquely.\n\n0.2.1-alpha1 fixes an issue with the 'sort' command syntax.",
    license='AGPLv3+',
    url='https://github.com/teward/imaplibext',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Communications :: Email',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='imaplib imap UID email'
)
