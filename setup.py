from setuptools import find_packages, setup


setup(
    name='imaplibext',
    version='0.1.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'typing',
    ],
    author='Thomas Ward',
    author_email='nathan@quickmediasolutions.com',
    description="Extend imaplib functions: Provide versions of IMAP4, IMAP4_SSL with UID-based message-set interaction "
                "functions instead of using the arbitrary message-numbering returned by the IMAP system.",
    license='GNU AGPL 3.0+',
    url='https://github.com/teward/imaplibext',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Other Environment'
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Communications :: Email',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
