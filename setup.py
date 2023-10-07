from setuptools import setup, find_packages

long_description = open('./README.md')

setup(
    name='Penv',
    version='1.1.1',
    url='https://github.com/ZSendokame/Penv',
    license='MIT license',
    author='ZSendokame',
    description='.env parser.',
    long_description=long_description.read(),
    long_description_content_type='text/markdown',

    packages=(find_packages(include=['penv']))
)