import codecs
import setuptools


setuptools.setup(
    name="capslock",
    version="0.0.1",
    author="Faruk Ahmad",
    author_email="faruk.csebrur@gmail.com",
    description="A high level python wrapper for processing text data.",
    long_description=codecs.open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/faruk-ahmad/capslock",
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    
)
