from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = open('README.md').read()



setup(

    name='pyrim', 

    version='1.0.1',

    description='A Simple and Efficient Image Manipulation Module',
    

    long_description=long_description,  

    long_description_content_type='text/markdown', 

    url='https://github.com/Rounik-Nikz/PyRim', 

    author='Rounik Mondal',  

    author_email='rounikmondal74@gmail.com',  

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],

    keywords='imageManipulation, image, pixels, rounik, pyrim',
    packages=find_packages(where='src'),
    python_requires='>=3.6, <4',
    install_requires=['Pillow'],
    package_dir={"": "src"},
    project_urls={
        'Source': 'https://github.com/Rounik-Nikz/PyRim',
    },
)