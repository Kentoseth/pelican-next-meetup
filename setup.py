from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pelican-next-meetup',
    version='0.1.1',
    description='Pelican plugin to get info on your next meetup.',
    long_description=long_description,
    url='https://github.com/SangSatori/pelican_next_meetup',
    author='Arnis Jaundžeikars',
    author_email='sangsatori@radiantmoons.me',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Operating System :: OS Independent',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',

        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='pelican plugins meetup',
    packages=find_packages(),
    install_requires=[
        'requests',
    ]
)
