from setuptools import setup, find_packages

setup(
    name="devopsdocker",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "flask==2.2.5",
        "werkzeug==2.2.3",
        "pytest==8.4.1"
    ],
)
