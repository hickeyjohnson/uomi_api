# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "uomi_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="UOMI API",
    author_email="mjh060@mun.ca",
    url="",
    keywords=["Swagger", "UOMI API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['uomi_server=uomi_server.__main__:main']},
    long_description="""\
    This API is to manage connections between clients and the UOMI backend.
    """
)

