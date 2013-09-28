# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='lingvista',
    author='Pijamas team',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
    zip_safe=False,
)