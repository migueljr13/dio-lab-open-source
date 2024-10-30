from setuptools import setup, find_packages

with open("README.md", "r") as f:
     page_description = f.read()
     
with open("requirements.txt") as f:
     requirements = f.read().splitlines()


setup(
    name="calculadora_cientifica",
    version="0.0.1",
    description="Uma simples calculadora científica em Python",
    author="Miguel Paulista",
    author_email="miguelpta@gmail.com",
    long_description=page_description,
    long_description_content_type="text/markdown"
    url="https://github.com/migueljr13/dio-lab-open-source"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.6'
)
