from setuptools import setup, find_packages

setup(
    name='labrary',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'asarPy==1.0.1',
        'asgiref==3.8.1',
        'Django==5.0.6',
        'djangorestframework==3.15.1',
        'pillow==10.3.0',
        'sqlparse==0.5.0',
    ],
    author='Mykhailo',
    author_email='zip.jpegg@gmail.com',
    description='Description of your project.',
    url='https://github.com/MXhch/Library',
)
