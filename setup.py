from setuptools import setup, find_packages

setup(
    name='amit_hook',
    version='0.0.3',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'magic = magic.main:main',
        ],
    },
)