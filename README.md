# AquilaDB-Python

Python client library for AquilaDB  

#### install

`pip install aquiladb`

#### usage

```
# import AquilaDB client
from aquiladb import AquilaClient as acl

# create DB instance
db = acl('localhost', 50051)

# convert a sample document
# convertDocument
sample = db.convertDocument([0.1,0.2,0.3,0.4], {"hello": "world"})

# add document to AquilaDB
db.addDocuments([sample])

# create a k-NN search vector
vector = db.convertMatrix([0.1,0.2,0.3,0.4])

# perform k-NN from AquilaDB
k = 10
result = db.getNearest(vector, k)
```

# AquilaDB

**AquilaDB** is a **Resillient**, **Replicated**, **Decentralized**, **Host neutral** storage for **Feature Vectors** along with **Document Metadata**. Do **k-NN** retrieval from anywhere, even from the darkest rifts of Aquila (in progress). It is easy to setup and scales as the universe expands.

Github: [https://github.com/a-mma/AquilaDB](https://github.com/a-mma/AquilaDB)

Docker Hub: [https://hub.docker.com/r/ammaorg/aquiladb](https://hub.docker.com/r/ammaorg/aquiladb)

Documentation (dedicated Wiki page): [https://github.com/a-mma/AquilaDB/wiki](https://github.com/a-mma/AquilaDB/wiki)

![constellation](http://astronomyonline.org/Observation/Images/Constellations/ConstellationBig/Aquila.gif)

#### Resillient
Make sure your data is always available anywhere through any network. It is not necessory to be always online. Work offline, sync later.

#### Replicated
Your data is replicated over nodes to attain eventual consistency. 

#### Decentralized
There is no single point of failure.

#### Host Neutral
Want to use AWS, Azure, G-cloud or whatever? Got a legion of laptops? Connect them together? No worries as long as they can talk each other.

# Who is this for
* If you are working on a data science project and need to store a hell lot of data and retrieve similar data based on some feature vector, this will be a useful tool to you, with extra benefits a real world web application needs.
* Are you dealing with a lot of images and related metadata? Want to find the similar ones? You are at the right place.
* If you are looking for a document database, this is not the right place for you.

# Technology
AquilaDB is not built from scratch. Thanks to OSS community, it is based on a couple of cool open source projects out there. We took a couch and added some wheels and jetpacks to make it a super cool butt rest for Data Science Engineers. While **CouchDB** provides us network and scalability benefits, **FAISS** provides superfast similarity search. Along with our peer management service, AquilaDB provides a unique solution.

created with ❤️ a-mma.indic (a_മ്മ)
