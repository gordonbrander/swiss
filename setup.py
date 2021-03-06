from setuptools import setup, find_packages
from os import path

readme_path = path.join(path.dirname(__file__), "README.md")
with open(readme_path) as f:
    readme = f.read()

setup(
    name='swiss',
    version='0.0.1',
    author='Gordon Brander',
    description='A command line utility for calculating layout grids',
    long_description=readme,
    license="GPL-3.0",
    url="https://github.com/gordonbrander/swiss",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.7",
    ],
    packages=find_packages(exclude=("tests", "tests.*")),
    install_requires=[],
    extras_require={},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'swiss_calc=swiss:swiss_calc'
        ]
    }
)
