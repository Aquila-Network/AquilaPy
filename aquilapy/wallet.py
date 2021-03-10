# Copyright (c) 2020.
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from Crypto.Hash import SHA384
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
import base58


class Wallet:
    def __init__ (self, key_file):
        # load pvt. key from key file
        self.priv_key = None
        with open(key_file, "r") as pkf:
            k = pkf.read()
            self.priv_key = RSA.import_key(k)

    def sign_bson_data (self, data_bson):
        # generate hash
        hash = SHA384.new()
        hash.update(data_bson)
        
        # Sign with pvt key
        signer = pkcs1_15.new(self.priv_key)
        signature = signer.sign(hash)
        signature = base58.b58encode(signature).decode("utf-8")

        return signature
