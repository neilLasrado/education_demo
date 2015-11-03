# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='education_demo',
    version=version,
    description='Demo for ERP For Education',
    author='Frappe Technologies',
    author_email='developers@frappe.io',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
