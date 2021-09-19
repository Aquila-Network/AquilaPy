<div align="center">
  <a href="https://aquila.network">
    <img
      src="https://user-images.githubusercontent.com/19545678/133918727-5a37c6be-676f-427b-8c86-dd50f58d1287.png"
      alt="Aquila Network Logo"
      height="64"
    />
  </a>
  <br />
  <p>
    <h3>
      <b>
        Aquila Py
      </b>
    </h3>
  </p>
  <p>
    <b>
      Python client to access Aquila Network Neural Search Engine
    </b>
  </p>
  <br/>
</div>

Here is a bird's eye view of where Aquila Client Libraries fit in the entire ecosystem:
<div align="center">
  <img
    src="https://user-images.githubusercontent.com/19545678/133918436-63c39f8a-aa6c-4d7c-939a-20e35cc8b2c2.png"
    alt="Aquila client libraries"
    height="400"
  />
 <br/>
</div>

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
