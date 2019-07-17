from __future__ import print_function

import grpc

import vecdb_pb2
import vecdb_pb2_grpc
name = "aquiladb"

channel = grpc.insecure_channel('localhost:50051')
stub = vecdb_pb2_grpc.VecdbServiceStub(channel)