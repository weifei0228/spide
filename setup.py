from setuptools import setup, find_packages

setup(name='spidetest',
      version='1.0',
      description='OpenShift App',
      author='Your Name',
      author_email='example@example.com',
      url='http://www.python.org/sigs/distutils-sig/',packages=find_packages(),
      install_requires=['flask>=0.10.1','bs4'],
     )
