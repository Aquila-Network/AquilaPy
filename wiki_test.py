from aquilapy import Wallet, DB, Hub
import numpy as np
import time

# Create a wallet instance from private key
wallet = Wallet("/Users/jubinjose/pem/private_unencrypted.pem")

host = "http://192.168.1.105"

# Connect to Aquila DB instance
db = DB(host, "5001", wallet)

# Connect to Aquila Hub instance
hub = Hub(host, "5002", wallet)

# Schema definition to be used
schema_def = {
    "description": "Wikipedia",
    "unique": "12345",
    "encoder": "ftxt:https://ftxt-models.s3.us-east-2.amazonaws.com/ftxt_base_min.bin",
    "codelen": 25,
    "metadata": {
        "url": "string",
        "text": "string"
    }
}

# Craete a database with the schema definition provided
db_name = db.create_database(schema_def)

# Craete a database with the schema definition provided
db_name_ = hub.create_database(schema_def)

print(db_name, db_name_)


# Download wiki dataset
# https://ftxt-models.s3.us-east-2.amazonaws.com/wikipedia_utf8_filtered_20pageviews.csv.gz
# Load file
import csv
docs = []
counter = 0
sup_counter = 0
query = None
with open('wiki.csv') as csvfile:
    while True:
        line = csvfile.readline()
        if not line or sup_counter >= 30:
            break

        line = line.split(",")
        article = [line[0], ",".join(line[1:])]

        for paragraph in article[1].split("\n"):
            print(sup_counter)
            paragraph = paragraph.strip()
            if paragraph != "":
                # print(sup_counter, counter, article[0])
                compression = hub.compress_documents(db_name, [paragraph])

                # reserve query vector
                if not query:
                    query = compression

                # Prepare documents to be inserted
                docs.append({
                    "metadata": {
                        "url": article[0], 
                        "text": paragraph
                    },
                    "code": compression[0]
                })

                if counter >= 10:
                    # Insert documents
                    dids = db.insert_documents(db_name, docs)
                    counter = 0
                else:
                    counter += 1
            else:
                print("empty")

        sup_counter += 1

time.sleep(60)
print("=====")
docs, dists = db.search_k_documents(db_name, query, 10)

print(docs, dists)