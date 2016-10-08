
from setuptools import setup, find_packages

setup(
        name='backend',
        version='0.1',
        packages=['backend'],
        zip_safe=False,
        include_package_data=True,
        install_requires=[
            'passlib', 
            'python-daemon', 
            'tornado', 
            'pyyaml', 
            'flask',
            'python-firebase',
            'WTForms']
)
