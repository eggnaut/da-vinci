from setuptools import find_packages
from distutils.core import setup
import os

setup(
	# Name of the package 
	name='EggEngine',
	# Packages to include into the distribution 
	packages=find_packages('.'),
	# Start with a small number and increase it with 
	# every change you make https://semver.org 
	version='0.0.1',
	# Chose a license from here: https: // 
	# help.github.com / articles / licensing - a - 
	# repository. For example: MIT 
	license='MIT',
	# Short description of your library 
	description='A custom framework/library written with and for Python.',
	# Long description of your library 
	# Your name 
	author='EggNaut',
	# Your email 
	author_email='',
	# Either the link to your github or to your website 
	url='https://github.com/eggnaut/EggEngine',
	# Link from which the project can be downloaded 
	download_url='https://github.com/eggnaut/EggEngine',
	# List of keywords 
	keywords=[],
	# List of packages to install with this one 
	install_requires=['cryptography','Pillow','setuptools', 'pygame'],
	# https://pypi.org/classifiers/ 
	classifiers=[]
)
