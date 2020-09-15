from setuptools import setup
from codecs import open
from os import path

SCRIPT_DIR = path.abspath(path.dirname(__file__))

with open(path.join(SCRIPT_DIR, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(SCRIPT_DIR, 'requirements.txt'), encoding='utf-8') as f:
    dependencies = f.read().splitlines()
    dependencies = filter(str, dependencies)
    dependencies = list(dependencies)

setup(
    name='cornershot',
    python_requires='>=3',
    version='0.0.1',
    description='Library to test network connectivity',
    long_description=long_description,
    url='https://github.com/zeronetworks/cornershot',
    author='Sagie Dulce, Zero Networks',
    author_email='support@zeronetworks.com',
    license='Apache v2',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='cornershot zerotrust ztna zeronetworks network scanner networkscanner',
    packages=['cornershot'],
    install_requires=dependencies,
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    }
)