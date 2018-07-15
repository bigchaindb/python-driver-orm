#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

install_requires = [
    "bigchaindb-driver==0.5.0",
]

setup(
    name='bigchaindb_orm',
    version='0.0.1',
    description="Python ORM for BigchainDB",
    long_description=readme,
    author="BigchainDB",
    author_email='dev@bigchaindb.com',
    url='https://github.com/bigchaindb/bigchaindb_orm',
    packages=find_packages(exclude=['tests*']),
    package_dir={
        'bigchaindb_orm': 'bigchaindb_orm'
    },
    include_package_data=True,
    install_requires=install_requires,
    python_requires='>=3.5',
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='bigchaindb_orm',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    extras_require={

    },
)
