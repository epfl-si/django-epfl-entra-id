from setuptools import setup
from io import open

setup(
    name='django-entraid',
    version='1.0.0',

    author='Lindo Duratti',
    author_email='lindo.duratti@epfl.ch',
    keywords='django, entraid, oidc, authentication',

    url='https://github.com/epfl-si/django-entraid',
    license="LGPLv3",
    description='A OIDC EntraID authentication backend for django',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',

    install_requires=[
        'mozilla-django-oidc==4.0.1',
        'python-dotenv==1.0.1',
        'requests==2.32.3',
        'django-login-required-middleware==0.9.0',
        'PyJWT==2.9.0',
    ],

    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: System :: Systems Administration :: Authentication/Directory',
    ]
)
