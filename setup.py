from setuptools import setup, find_packages

setup(
    name='pylambdic',
    version='1.0.0',
    author='Agustin Marchi',
    url='https://github.com/agusmdev/pylambdic',
    packages=find_packages(),
    license='LICENSE',
    description='Validate input and output for AWS Lambda handlers using Pydantic',
    long_description=open('README.md').read(),
    python_requires='>=3.7',
    install_requires = [
        "pydantic>=1.10.7"
    ],
)
