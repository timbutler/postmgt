import os
from setuptools import setup, find_packages

setup(
    name='postmgt',
    version='0.1',
    install_requires=['blessings', 'docopt'],
    url='https://github.com/timbutler/postmgt',
    license='GPL 2',
    author='Tim Butler',
    author_email='tim.butler.au+github@gmail.com',
    description='Basic Postfix queue management for rapid deletion of emails',
    long_description=open("README.md").read(),
    packages=find_packages(),

    scripts=['postmgt'],
    classifiers=[
        'Programming Language :: Python',
        'Intended Audience :: System Administrators',
        'Topic :: Communications :: Email',
    ]
)
