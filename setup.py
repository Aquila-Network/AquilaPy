import setuptools

# load README content
with open("README.md", "r") as fh:
    long_description = fh.read()

# setup package
setuptools.setup(
    name='aquiladb',  
    version='0.5.1',
    author="Harold Gomez",
    author_email="haroldgmz11@gmail.com",
    description="Python client library for AquilaDB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/a-mma/AquilaDB-Python",
    packages=setuptools.find_packages(),
    install_requires=[
      'grpcio',
      'protobuf'
    ],
    classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
    ],
)