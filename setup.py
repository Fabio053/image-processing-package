from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(

    name="image_processing-package",
    version="0.0.1",
    author="my_name",
    author_email="my_email",
    description="Pacote de processamento de images da DIO",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Fabio053/image-processing-package.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8'
)