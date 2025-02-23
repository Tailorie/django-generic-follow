#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-generic-follow',
    version='0.6.0',
    description='Generic follow system for Django',
    long_description=open('README.rst').read(),
    author='Gizmag',
    author_email='tech@gizmag.com',
    url='https://github.com/Tailorie/django-generic-follow',
    packages=find_packages(exclude=['tests']),
    install_requires=['django >= 1.8'],
    test_suite='runtests.runtests',
    tests_require=['django', 'django_nose']
)
