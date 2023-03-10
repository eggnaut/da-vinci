#    An all-purpose framework/library written with and for Python.
#    Copyright (C) 2023  Dishant B. (eggnaut)
#
#    This library is free software; you can redistribute it and/or
#    modify it under the terms of the GNU Lesser General Public
#    License as published by the Free Software Foundation; either
#    version 2.1 of the License, or (at your option) any later version.
#
#    This library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with this library; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
#    USA

'''
Part of da vinci.

Usage: 'from davinci import module' or 'import davinci.module'

Includes functions to install dependencies for da vinci as well as functions relating to Python packages.

Made by @eggnaut
'''

import sys
import subprocess as sp
import platform as pm

def autoUpdate(pip: str | None, path: str) -> None:
    '''
    Automatically updates all Python packages listed in a file.

    Args:
        pip (str | None): for macOS: pip3, for Windows: pip, this is a terminal/shell command
        path (str): the path to the file (preferably .txt) where the package names are listed (one per line)
    '''
    
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            
            for line in range(lines):
                package = line.readline()
                
                if pip:
                    try:
                        sp.call(f'{pip} install {package}', shell = True)
                    except:
                        print(f'\ndavinci.module.autoUpdate() was unable to update the packages.\nError: {package} doesn\'t exist.\nPlease make sure the package name provided is correct.\n')
                        sys.exit(1)
                else:
                    try:
                        if pm.system() == 'Windows':
                            sp.call(f'pip install --upgrade {package}', shell = True)
                        elif pm.system() == 'Darwin' or pm.system() == 'Linux':
                            sp.call(f'pip3 install --upgrade {package}', shell = True)
                    except:
                        print(f'\ndavinci.module.autoUpdate() was unable to update the packages.\nError: {package} doesn\'t exist.\nPlease make sure the package name provided is correct.\n')
                        sys.exit(1)
        
            file.close()
    except FileNotFoundError:
        print(f'\ndavinci.module.autoUpdate() was unable to open the file.\nError: {path} doesn\'t exist.\nPlease make sure the path provided is correct.')
        sys.exit(1)

def autoInstall(pip: str | None, path: str) -> None:
    '''
    Automatically installs all Python packages listed in a file.

    Args:
        pip (str | None): for macOS: pip3, for Windows: pip, this is a terminal/shell command
        path (str): the path to the file (preferably .txt) where the package names are listed (one per line)
    '''
    
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            
            for line in range(lines):
                package = line.readline()
                
                if pip:
                    try:
                        sp.call(f'{pip} install {package}', shell = True)
                    except:
                        print(f'\ndavinci.module.autoInstall() was unable to install the packages.\nError: {package} doesn\'t exist.\nPlease make sure the package name provided is correct.\n')
                        sys.exit()
                else:
                    if pm.system() == 'Windows':
                        sp.call(f'pip install {package}', shell = True)
                    elif pm.system() == 'Darwin' or pm.system() == 'Linux':
                        sp.call(f'pip3 install {package}', shell = True)
            file.close()
    except FileNotFoundError:
        print(f'\ndavinci.module.autoInstall() was unable to open the file.\nError: {path} doesn\'t exist.\nPlease make sure the path provided is correct.')
        sys.exit(1)

def dependencies(pip: str | None) -> None:
    '''
    Installs the required modules/dependencies that this engine/framework requires.

    Args:
        pip (str | None, optional): for macOS: pip3, for Windows: pip, this is a terminal/shell command
    '''
    
    if pip:
        try:
            sp.call(f'{pip} install pygame', shell = True)
            sp.call(f'{pip} install cryptography', shell = True)
            sp.call(f'{pip} install pillow', shell = True)
        except:
            print(f'\ndavinci.module.dependencies() was unable to install dependencies.\nError: {pip} is not a valid shell command.\nPlease make sure the pip type (pip or pip3) provided is correct.\n')
            sys.exit(1)
    else:
        if pm.system() == 'Windows':
            sp.call('pip install pygame', shell = True)
            sp.call('pip install cryptography', shell = True)
            sp.call('pip install pillow', shell = True)
        elif pm.system() == 'Darwin' or pm.system() == 'Linux':
            sp.call('pip3 install pygame', shell = True)
            sp.call('pip3 install cryptography', shell = True)
            sp.call('pip3 install pillow', shell = True)

def updateAll(pip: str | None) -> None:
    '''
    Updates all installed modules without the hassle of this once tedious task.

    Args:
        pip (str | None, optional): for macOS: pip3, for Windows: pip, this is a terminal/shell command
    '''
    
    if pip:
        try:
            sp.call(f'{pip} list --outdated > outdated.txt', shell = True)
        except:
            print(f'\ndavinci.module.updateAll() was unable to update modules.\nError: {pip} is not a valid shell command.\nPlease make sure the pip type (pip or pip3) provided is correct.\n')
            sys.exit(1)
    else:
        if pm.system() == 'Windows':
            sp.call('pip list --outdated > outdated.txt', shell = True)
        elif pm.system() == 'Darwin' or pm.system() == 'Linux':
            sp.call('pip3 list --outdated > outdated.txt', shell = True)

    with open('outdated.txt', 'r') as file:
        file.readline()
        file.readline()

        while True:
            package = file.readline()

            if package.split():
                name = package.split()[0]
                if pip:
                    sp.call(f'{pip} install --upgrade {name}' , shell = True)
                else:
                    if pm.system() == 'Windows':
                        sp.call('pip install --upgrade {name}' , shell = True)
                    elif pm.system() == 'Darwin' or pm.system() == 'Linux':
                        sp.call('pip3 install --upgrade {name}' , shell = True)
                        
            elif not package:
                break

        file.close()