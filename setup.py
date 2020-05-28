#!/usr/bin/env python

from distutils.core import setup

setup(name='GRU4REC',
      version='1.0',
      description='GRU for recommnedations',
      author='hidasib',
      author_email='notsure.net',
      url='https://github.com/riggs23/mygru',
      packages=['gru4rec', 'gpu_ops', 'evaluation', 'datatools', 'custom_theano_ops'],
     )
