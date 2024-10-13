# setup.py

from setuptools import setup, find_packages

setup(
    name='hash_maker',
    version='0.1.0',
    author='Charan A A',
    author_email='mariswarycharan@gmail.com',
    description='A secure password hashing package using PyNaCl',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mariswarycharan/Password_hashing_PIP_folder',
    packages=find_packages(),
    install_requires=[
        'pynacl>=1.3.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Security :: Cryptography',
    ],
    python_requires='>=3.6',
)
