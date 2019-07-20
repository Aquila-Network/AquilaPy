# Copyright (c) 2019-present, a_മ്മ.
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import grpc

from aquiladb import vecdb_pb2
from aquiladb import vecdb_pb2_grpc

import base64
import json

class AquilaClient:
    def __init__(self, root_url, port):
        self.channel = grpc.insecure_channel(root_url + ':' + str(port))
        self.stub = vecdb_pb2_grpc.VecdbServiceStub(self.channel)
    
    # API interface to add documents to AquilaDB
    def addDocuments (self, documents_in):
        response = self.stub.addDocuments(vecdb_pb2.addDocRequest(documents=documents_in))
        return response

    # API interface to get nearest documents from AquilaDB
    def getNearest (self, matrix_in, k_in):
        response = self.stub.getNearest(vecdb_pb2.getNearestRequest(matrix=matrix_in, k=k_in))
        return response

    # helper function to convert native data to API friendly data
    def convertDocuments(self, vector, document):
        return {
            "vector": {
                "e": vector
            },
            "b64data": json.dumps(document, separators=(',', ':')).encode('utf-8')
        }

    # helper function to convert native data to API friendly data
    def convertMatrix(self, vector):
        return [{
                "e": vector
        }]