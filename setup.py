import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
#CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

setup(
    name='python-webdev',
    version='0.0.1',
    description='Python base project for web development',
    #long_description=README + '\n\n' + CHANGES,
    long_description=README,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='Øystein S. Haaland',
    author_email='oystein.s.haaland@gmail.com',
    url='',
    keywords='web wsgi pyramid',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    #test_suite='pythonservice',
    install_requires=[
        'uwsgi',
        'pyramid',
        'invoke',
    ],
    #entry_points="""\
    #[paste.app_factory]
    #main = pythonservice:main
    #[console_scripts]
    #initialize_pythonservice_db = pythonservice.scripts.initializedb:main
    #""",
)
