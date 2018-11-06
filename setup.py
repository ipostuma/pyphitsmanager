#!python
import sys, os, subprocess

# prepare setuptools environment
try:
    from setuptools import setup, find_packages
except ImportError:
    print "Could NOT import setuptools, try ez_setup..."
    try:
        from ez_setup import use_setuptools
        use_setuptools()
        from setuptools import setup, find_packages
    except ImportError:
        print "Could NOT import either setuptools or ez_setup, GIVE UP!"
        print "Download ez_setup.py e.g. " \
            "from https://bootstrap.pypa.io/ez_setup.py,"
        print "place it in the same directory as setup.py, and try again... "
        sys.exit(1)

setup(
    # Application name:
    name="PHITSmanager",

    # Version number (initial):
    version="0.1.1",
    license = "GNU GPL v3",

    # Application author details:
    author="Ian Postuma",
    author_email="ian.postuma@gmail.com",

    # Packages
    packages = find_packages(),
    # Include additional files into the package
    include_package_data=True,

    # Details
    url="https://github.com/ipostuma/pyphitsmanager",

    #
    # license="LICENSE.txt",
    description="""PHITS file project Manager
    This program aims to help developing and managing an PHITS simulation""",

    scripts=['bin/PHITSmanager'],

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    #  install_requires=[
    #      "shutil", "sys", "argparse", "string", "os"
    #  ],
)
