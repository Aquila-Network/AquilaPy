# AquilaDB-Python

Python client library for Aquila Network

#### install

`pip install aquilapy`

#### Tutorial

```
from aquilapy import Wallet, DB
import numpy as np

# Create a wallet instance from private key
wallet = Wallet("<path to>/openssl/private_unencrypted.pem")

# Connect to a running AquilaDB instance
db = DB("http://127.0.0.1", "5000", wallet)

# Schema definition to be used
schema_def = {
    "description": "this is my database",
    "unique": "r8and0mseEd901",
    "encoder": "example.com/autoencoder/API",
    "codelen": 3,
    "metadata": {
        "name": "string",
        "age": "number"
    }
}

# Craete a database with the schema definition provided
db_name = db.create_database(schema_def)

# Prepare documents to be inserted
docs = [{
    "metadata": {
        "name":"name1", 
        "age": 20
    },
    "code": [1,2,3]
}, {
        "metadata": {
        "name":"name2", 
        "age": 30
    },
    "code": [1,2,3]
}]

# Insert documents
dids = db.insert_documents(db_name, docs)

print(dids)

# Delete some documents
dids = db.delete_documents(db_name, dids)

print(dids)

# Perform a similarity search operation
matrix = np.random.rand(1, 784).tolist()

docs, dists = db.search_k_documents(db_name, matrix, 10)

print(len(docs[0]), len(dists[0]))
```

created with ❤️ a-mma.indic (a_മ്മ)
