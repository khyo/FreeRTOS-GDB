# Copyright (c) 2017 Kyle Howen
# All Rights Reserved.

import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name='FreeRTOS-GDB',
    version='1.0.0',
    description='Python API Library for inspecting FreeRTOS Objects in GDB',
    packages='freertos_gdb',
    license='GPLV2',
    url='https://github.com/autolycus/FreeRTOS-GDB',
    author='Carl Allendorph',
    author_email='kyle.howen@subinitial.com',
    long_description=read("README.md"),
    classifiers = [
        # 'Development Status :: 4 - Beta',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2'
    ]
)
