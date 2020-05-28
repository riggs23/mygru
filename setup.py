from setuptools import find_packages, setup


# Import version
#__builtins__.__SPOTLIGHT_SETUP__ = True
#from spotlight import __version__ as version  # NOQA


setup(
    name='gru4rec',
    packages=find_packages(),
    classifiers=['Development Status :: 3 - Alpha',
                 'Topic :: Scientific/Engineering :: Artificial Intelligence'],
)
