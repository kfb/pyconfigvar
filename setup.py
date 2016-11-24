"""Setuptools module."""

import os

from setuptools import (
    find_packages,
    setup,
)


README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md')
with open(README_PATH) as f:
    long_description = f.read()

setup(
    name='pyconfigvar',
    version='1.0.0',
    description='Manage required and optional environment variables in your scripts.',
    long_description=long_description,
    url='https://github.com/kfb/pyconfigvar',
    author='kfb',
    author_email='kaleidoscopicfilmstripblues@gmail.com',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
    ],
    keywords='environment',
    packages=find_packages(),
    install_requires=[],
)
