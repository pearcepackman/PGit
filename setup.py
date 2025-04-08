from setuptools import setup, find_packages

setup(
    name = 'pgit',
    version = '0.1',
    packages = find_packages(),
    entry_points = {
        'console_scripts': [
            'pgit=pgit.cli',
            ],
        },
)