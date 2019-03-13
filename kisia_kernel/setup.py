#!/usr/bin/env python

from distutils.core import setup

setup(
    name='KISIA Python Toolkit Kernel',
    version='0.1',
    description='KISIA Python Toolkit Kernel',
    author='Korsimoro',
    author_email='eric@korsimoro.com',
    url='none-yet',
    packages=[
		'kisia_kernel'
		],
    install_requires=[
        'ipykernel',
        'KISIA-Python-Toolkit',
        'jupyter_kernel_test'
    ],
    entry_points = {
    }
)
