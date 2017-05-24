# !./env/bin/python

from __future__ import absolute_import
from setuptools import setup, find_packages


setup(
    name='refunite-drc-admin',
    version='1.0.0',
    author="Tobias Sauerwein",
    author_email='ts@refunite.org',
    url="https://git.refunite.org/scm/in/refunite-user-api-client.git",  # noqa
    keywords="reverse-geocoding drc congo admin-level territory",
    description="Get the DRC territory from a coordinate.",
    include_package_data=True,
    packages=find_packages(exclude=("tests")),
    zip_safe=False,
    license='MIT License',
    test_suite="tests",
    install_requires=[
        "geojson==1.3.5",
        "Shapely==1.6b4"
    ],
    dependency_links=[],
)
