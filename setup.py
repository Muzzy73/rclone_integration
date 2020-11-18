# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in rclone_integration/__init__.py
from rclone_integration import __version__ as version

setup(
	name='rclone_integration',
	version=version,
	description='Frappe integration with rclone',
	author='9T9IT',
	author_email='info@9t9it.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
