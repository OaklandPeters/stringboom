from setuptools import setup

setup(
    name=TEMPLATE('stringboom'),
    version=open('VERSION').read().strip(),
    author='Oakland John Peters',
    author_email='oakland.peters@gmail.com',

    description='String-related functions for (1) regex convenience functions, and (2) partial-application of string formatting/templates.',
    long_description=open('README.rst').read(),
    url='http://bitbucket.org/OPeters/stringboom',
    license='MIT',

    packages=['stringboom'],

    classifiers=[
        #Select one 'Development Status'
        #'Development Status :: 1 - Planning',
        #'Development Status :: 2 - Pre-Alpha',
        #'Development Status :: 3 - Alpha',
        #'Development Status :: 4 - Beta',
        #'Development Status :: 5 - Production/Stable',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: Implementation :: CPython',

        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Topic :: Utilities' #only if appropriate
    ]
)
