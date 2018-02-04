# -*- coding: utf-8 -*-
import os
from setuptools import setup
from setuptools import find_packages

# meta info
NAME = "dtwalign"
VERSION = "0.0.6"
AUTHOR = "Takehiro Suzuki"
AUTHOR_EMAIL = ""
URL = "https://github.com/statefb/dtwalign"
DESCRIPTION = 'Comprehensive DTW package which enables partial mathing and has various constraint options'
LICENSE = "GPL v2"

if not os.path.exists('README.txt'):
    os.system("pandoc -o README.txt README.md")
LONG_DESCRIPTION = open('README.txt').read()

def main():

    setup(
        name=NAME,
        version=VERSION,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        url=URL,
        description=DESCRIPTION,
        long_description = LONG_DESCRIPTION,
        zip_safe=False,
        include_package_data=True,
        packages=find_packages(),
        install_requires=[
            "numpy",
            "matplotlib",
            "seaborn >= 0.8.1",
            "networkx",
            "numba >= 0.34.0",
            "scipy"
        ],
        dependency_links = [

        ],
        tests_require=[],
        setup_requires=[],
        license=LICENSE,
        classifiers = [
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
            "Topic :: Scientific/Engineering",
        ]
    )


if __name__ == '__main__':
    main()
