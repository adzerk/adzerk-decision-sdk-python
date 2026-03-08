# coding: utf-8

"""
    Adzerk Decision API
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "adzerk-decision-sdk"
VERSION = "1.0.0-beta.21"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 2.0.0", "six >= 1.10", "certifi >= 2023.7.22", "python-dateutil >= 2.8.2"]

setup(
    name=NAME,
    version=VERSION,
    description="Adzerk Decision SDK",
    author="Adzerk",
    author_email="engineering@adzerk.com",
    url="https://github.com/adzerk/adzerk-decision-sdk-python",
    keywords=["adzerk", "Adzerk Decision SDK"],
    python_requires='>=3.10',
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    Adzerk Decision SDK
    Python Software Development Kit for Adzerk Decision & UserDB APIs
    https://github.com/adzerk/adzerk-decision-sdk-python
    """
)
