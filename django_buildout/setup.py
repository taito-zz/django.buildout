from setuptools import find_packages
from setuptools import setup


setup(
    name='django_buildout',
    version='0.0.1',
    description="",
    long_description='',
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"],
    keywords='',
    author='Taito Horiuchi',
    author_email='taito.horiuchi@gmail.com',
    url='https://github.com/taito/django_buildout',
    license='FreeBSD',
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools'],
    entry_points="""
    # -*- Entry points: -*-
    """)