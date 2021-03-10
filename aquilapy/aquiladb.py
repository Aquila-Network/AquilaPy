# Copyright (c) 2020.
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import requests
from requests.structures import CaseInsensitiveDict
import json, bson

class DB:
    def __init__(self, host, port, wallet):
        self.host = host
        self.port = port
        self.url = host + ":" + port
        self.wallet = wallet

        # try connecting to AquilaDB
        resp = self.mkrequest("/", {}, "GET")

        if resp.json()["success"]:
            print(resp.json()["message"])
        
    def mkrequest (self, endpoint, signed_data, req_type):
        url = self.url + endpoint
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"

        data = json.dumps(signed_data)

        if req_type == "GET":
            return requests.get(url, headers=headers, data=data)
        elif req_type == "POST":
            return requests.post(url, headers=headers, data=data)

    # Create a database from schema definition
    def create_database (self, schema):
        data_ = { "schema": schema }
        data_bson = bson.dumps(data_)
        signature = self.wallet.sign_bson_data(data_bson)

        data = {
            "data": data_,
            "signature": signature
        }

        resp = self.mkrequest("/db/create", data, "POST")
        
        if resp.json()["success"]:
            return resp.json()["database_name"]
        else:
            return None

    # Parse and sign each document in the documents array
    def sign_documents (self, documents):
        ret_docs = []

        for doc in documents:
            data_bson = bson.dumps(doc)
            signature = self.wallet.sign_bson_data(data_bson)
            data = {
                "payload": doc,
                "signature": signature
            }
            ret_docs.append(data)

        return ret_docs


    # Insert docs according to schema definition
    def insert_documents (self, database_name, documents):
        # sign each document
        documents = self.sign_documents(documents)

        data_ = { "docs": documents, "database_name": database_name }
        data_bson = bson.dumps(data_)
        signature = self.wallet.sign_bson_data(data_bson)

        data = {
            "data": data_,
            "signature": signature
        }

        resp = self.mkrequest("/db/doc/insert", data, "POST")
        
        if resp.json()["success"]:
            return resp.json()["ids"]
        else:
            return None

    # Delete documents
    def delete_documents (self, database_name, doc_ids):
        data_ = { "ids": doc_ids, "database_name": database_name }
        data_bson = bson.dumps(data_)
        signature = self.wallet.sign_bson_data(data_bson)

        data = {
            "data": data_,
            "signature": signature
        }

        resp = self.mkrequest("/db/doc/delete", data, "POST")
        
        if resp.json()["success"]:
            return resp.json()["ids"]
        else:
            return None

    # Search k documents
    def search_k_documents (self, database_name, matrix, k):
        data_ = { "matrix": matrix, "k": k, "database_name": database_name }
        data_bson = bson.dumps(data_)
        signature = self.wallet.sign_bson_data(data_bson)

        data = {
            "data": data_,
            "signature": signature
        }

        resp = self.mkrequest("/db/search", data, "GET")
        
        if resp.json()["success"]:
            return resp.json()["docs"], resp.json()["dists"]
        else:
            return None
        