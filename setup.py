#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from tox_irc_bridge import __version__

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'pytox',
]

test_requirements =  requirements + [
    'flake8',
    'tox',
    'coverage',
]

setup(
    name='tox_irc_bridge',
    version=__version__,
    description="Tox IRC bridge to relay messages",
    long_description=readme,
    author="Jon Robison",
    author_email='narfman0@gmail.com',
    url='https://github.com/narfman0/tox_irc_bridge',
    packages=[
        'tox_irc_bridge',
    ],
    package_dir={'tox_irc_bridge':
                 'tox_irc_bridge'},
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='tox_irc_bridge',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
