# Copyright (c) 2020.
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import requests
from requests.structures import CaseInsensitiveDict
import json, bson

class Hub:
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

        resp = self.mkrequest("/prepare", data, "POST")
        
        if resp.json()["success"]:
            return resp.json()["databaseName"]
        else:
            return None

    # Compress document according to model
    def compress_documents (self, database_name, text_list):
        data_ = { "databaseName": database_name, "text": text_list }

        data = {
            "data": data_
        }

        resp = self.mkrequest("/compress", data, "POST")
        
        if resp.json()["success"]:
            return resp.json()["vectors"]
        else:
            return None
        