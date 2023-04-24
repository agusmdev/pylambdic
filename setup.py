from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='pylambdic',
    version='1.0.0',
    author='Agustin Marchi',
    author_email='agusmdev@gmail.com',
    description='Validate input and output for AWS Lambda handlers using Pydantic',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/agusmdev/pylambdic',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.7',
    install_requires=[
        'pydantic>=1.10.7',
    ],
)