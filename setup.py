from setuptools import setup
from setuptools import find_packages

setup(name='DSPP-Keras',
      version='0.0.3',
      description='Integration of DSPP database with Keral Machine Learning Library',
      author='Jan Domanski',
      author_email='jan@peptone.io',
      url='https://github.com/PeptoneInc/dspp-keras',
      download_url='https://github.com/PeptoneInc/dspp-keras/archive/v0.0.3.tar.gz',
      license='MIT',
      install_requires=['keras', 'numpy', 'h5py'],
      packages=find_packages())
