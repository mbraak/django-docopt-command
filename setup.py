from setuptools import setup, find_packages


version = '0.1.0'

setup(
    name='django-docopt-command',
    version=version,
    packages=find_packages(),
    license='Apache License, Version 2.0',
    include_package_data=True,
    zip_safe=False,
    author='Marco Braak',
    author_email='mbraak@ridethepony.nl',
    install_requires=['django', 'docopt'],
    description='Django-docopt-command allows you to write Django manage.py commands using the docopt library',
)