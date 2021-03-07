# AquilaDB-Python

Python client library for Aquila Network

#### install

`pip install aquilapy`

#### Tutorial

```python
from aquilapy import Wallet, DB, Hub
import numpy as np
import time

# Create a wallet instance from private key
wallet = Wallet("private_unencrypted.pem")

host = "http://127.0.0.1"

# Connect to Aquila DB instance
db = DB(host, "5001", wallet)

# Connect to Aquila Hub instance
hub = Hub(host, "5002", wallet)

# Schema definition to be used
schema_def = {
    "description": "this is my database",
    "unique": "r8and0mseEd901",
    "encoder": "ftxt:https://ftxt-models.s3.us-east-2.amazonaws.com/ftxt_base_min.bin",
    "codelen": 25,
    "metadata": {
        "name": "string",
        "age": "number"
    }
}

# Craete a database with the schema definition provided
db_name = db.create_database(schema_def)

# Craete a database with the schema definition provided
db_name_ = hub.create_database(schema_def)

print(db_name, db_name_)

# Generate encodings
texts = ["Amazon", "Google"]
compression = hub.compress_documents(db_name, texts)
print(compression)

# Prepare documents to be inserted
docs = [{
    "metadata": {
        "name":"name1", 
        "age": 20
    },
    "code": compression[0]
}, {
        "metadata": {
        "name":"name2", 
        "age": 30
    },
    "code": compression[1]
}]

# Insert documents
dids = db.insert_documents(db_name, docs)

print(dids)

# Delete some documents
dids = db.delete_documents(db_name, dids)

print(dids)

# Perform a similarity search operation
matrix = np.random.rand(1, 25).tolist()

time.sleep(5)

docs, dists = db.search_k_documents(db_name, matrix, 10)

print(len(docs[0]), len(dists[0]))
```

created with ❤️ a-mma.indic (a_മ്മ)
