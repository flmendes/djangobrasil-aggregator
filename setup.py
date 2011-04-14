from setuptools import setup, find_packages

setup(name='aggregator',
        version='1',
        description='Django pluggable agrregator',
        author='Eric Woudenberg',
        packages=find_packages(),
        classifiers=['Development Status :: 1',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Utilities'],
    include_package_data=True,
    install_requires=['setuptools'],
)