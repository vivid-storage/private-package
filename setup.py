from setuptools import setup, find_packages

setup(
    name="dummy_pkg",
    version="0.1.0",
    description="A dummy package that doesn't do anything",
    author="Tester",
    author_email="test@example.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
