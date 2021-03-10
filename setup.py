import setuptools

# load README content
with open("README.md", "r") as fh:
    long_description = fh.read()

# setup package
setuptools.setup(
    name='aquilapy',  
    version='0.3.1',
    author="Aquila Network",
    author_email="contact@aquila.network",
    description="Python client library for Aquila Network",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Aquila-Network/aquilapy",
    packages=setuptools.find_packages(),
    install_requires=[
    "bson",
    "requests",
    "pycryptodome",
    "base58"
    ],
    classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
    ],
)
