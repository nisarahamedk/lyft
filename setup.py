import os, sys
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

def read_requirements():
    """Parse requirements from requirements.txt."""
    reqs_path = os.path.join('.', 'requirements.txt')
    with open(reqs_path, 'r') as f:
        requirements = [line.rstrip() for line in f]
    return requirements

setuptools.setup(
    name="lyft", # Replace with your own username
    version="0.0.1",
    author="Nisar Ahamed K",
    author_email="nisar009@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nisarahamedk/lyft",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=read_requirements(),
)
