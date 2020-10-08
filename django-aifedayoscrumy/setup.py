import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
setup(
    name="aifedayoscrumy", # Replace with your own username
    version="0.1",
    packages = find_packages(),
    include_package_data = True,
    licence = 'BSD Licence',
    description = "A simple chat application thats uses aws and websockets",
    long_description = README,
    url ="https://www.example.com/",
    author="Akeem Lagundoye",
    author_email="akeemifedayolag@gmail.com",
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: X,Y',
        "Intended Audience :: Developers",
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)