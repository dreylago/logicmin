from setuptools import setup, find_packages
from os import path
from codecs import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='logicmin',
      version='0.4.0',
      description='Logic Minimization',
      url='http://github.com/dreylago/logicmin',
      author='Demetrio Rey',
      author_email='demetrio.rey@gmail.com',
      license='MIT',
      packages=['logicmin'],
      install_requires=['future'],
      python_requires='>=2.7',
      zip_safe=False,
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)',
      ],
      long_description=long_description,
      include_package_data=True,
      )
