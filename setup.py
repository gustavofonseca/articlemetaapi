#!/usr/bin/env python
from setuptools import setup, find_packages

install_requires = [
    'thriftpy>=0.3.1',
    'requests>=2.8.1',
    'xylose'
]

tests_require = []

setup(
    name="articlemetapi",
    version="0.1.0",
    description="Library that implements the endpoints of the ArticleMeta API",
    author="SciELO",
    author_email="scielo-dev@googlegroups.com",
    maintainer="Fabio Batalha",
    maintainer_email="fabio.batalha@scielo.org",
    url="http://github.com/scieloorg/processing",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.7",
    ],
    dependency_links=[
        "git+https://git@github.com/scieloorg/xylose.git@v1.16.5#egg=xylose"
    ],
    tests_require=tests_require,
    test_suite='tests',
    install_requires=install_requires
)