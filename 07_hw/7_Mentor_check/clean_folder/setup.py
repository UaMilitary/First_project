from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.1',
    description='sort files in folders',
    author='Alexx133123',
    entry_points={'console_scripts': ['clean=clean_folder.clean:start']}
)
