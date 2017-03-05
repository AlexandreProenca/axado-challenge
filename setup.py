#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys
import shutil

from setuptools import setup


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    Retorna a versão do pacote listada na variável `__version__` no arquivo `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def get_packages(package):
    """
    Return root package and all sub-packages.
    Retorna a Raiz do pacote com todos seus sub-diretorios.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    Retornar todos os arquivos no pacote raiz, que não estão em um
    próprio pacote.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}

version = get_version('axado_calculator')

# The few arguments to easily deploy
# Argumentos que facilitam na hora de publicar o pacote em produção

if sys.argv[-1] == 'publish':
    if os.system("pip freeze | grep wheel"):
        print("wheel not installed.\nUse `pip install wheel`.\nExiting.")
        sys.exit()
    if os.system("pip freeze | grep twine"):
        print("twine not installed.\nUse `pip install twine`.\nExiting.")
        sys.exit()
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    shutil.rmtree('dist')
    shutil.rmtree('build')
    shutil.rmtree('axado-challenge.egg-info')
    sys.exit()


setup(
    name='axado-challenge',
    version=version,
    url="https://github.com/AlexandreProenca/axado-challenge",
    license='MIT',
    description='This is a challenge job for Axado company',
    author='Alexandre Proença',
    author_email='alexandre.proenca@hotmail.com.br',
    packages=get_packages('axado_calculator'),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'axado_calculator=axado_calculator.axado_calculator:main',
        ],
    },
    zip_safe=False,
    keywords='Shell Calculator',


    package_data={

    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Shell Environment',
        'Framework :: Pure Python',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Calculator :: Shell',
    ]
)
