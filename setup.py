#pip install -e .
from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst')) as f:
    LONG_DESCRIPTION = f.read()
    
CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Topic :: Security :: Cryptography",
]

setup(name='wpa2slow',
      version='0.4',
      description='A full Python implementation of the WPA2 encryption algorithm, using no encryption libraries.',
      long_description=LONG_DESCRIPTION,
      url='http://github.com/JarrettR/WPA-Slowed-Down',
      author='Jarrett Rainier',
      author_email='jrainier@gmail.com',
      license='GPLv3',
      packages=['wpa2slow'],
      classifiers=CLASSIFIERS,
      zip_safe=False)
