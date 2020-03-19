from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    author='kan',
    install_requires=[
        'requests',
    ],
    name="kan_sdk",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    url="https://github.com/kan-fun/kan-python",
    version="0.0.1",
)