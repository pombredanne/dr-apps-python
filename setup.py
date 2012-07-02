#!/usr/bin/env python

from setuptools import setup

setup(name='drcli',
      version='0.1',
      description='Command-line tools for docrep',
      author = 'schwa lab',
      url='http://schwa.org/git/drcli.git',
      packages=['drcli'],
      scripts=['dr'],
      install_requires=['argparse'],
      package_data = {
        'drcli': ['plugins/*/*.py'],
      },
      license='Apache 2.0',
     )
