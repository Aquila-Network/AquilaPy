
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='aquiladb',  
     version='0.2',
     scripts=['vecstore'] ,
     author="Jubin Jose",
     author_email="hello@josejub.in",
     description="Vecstore package for AquilaDB",
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
