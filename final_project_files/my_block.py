import hashlib
import os
import json
import datetime
from blockchain import Blockchain

class Block:

    def block_header(self): #This needs to be a string since hash will be ran through encode
        return str(self.index) + self.prev_hash + self.data + str(self.timestamp) + str(self.nonce)
    
    def hash_generator(self):
        result = hashlib.sha256(self.block_header().encode())
        #print(result)
        return result.hexdigest()
    
    def self_save(self): #saves the blockchain state locally to the node
        chaindata_dir = 'chaindata'
        index_string = str(self.index).zfill(6) #adds leading 0s to the filename
        filename = '%s/%s.json' % (chaindata_dir, index_string)

        #Adding this in to allow potential corruption of data

        if(os.path.exists(filename)):
            os.remove(filename)

        with open(filename, 'w') as block_file:
            json.dump({"index":self.index,"timestamp":str(self.timestamp),"data":self.data,"nonce":self.nonce,"hash":self.hash,"prev_hash":self.prev_hash}, block_file)

    def __init__(self, index, timestamp, prev_hash, data, nonce, hash = None):
        self.index = index
        self.timestamp = timestamp
        self.prev_hash = prev_hash
        self.data = data
        self.nonce = nonce #increments to satisfy PoW concept
        
        #Differentiates when a new block is created or not
        if hash is not None:
            self.hash = hash
        else:
            self.hash = self.hash_generator()

        #print(self.hash)

    # This method checks to see whether a block is equal to a "different" input block.
    def are_blocks_equal(self, other_block):
        return ( (self.index == other_block.index) and (self.timestamp == other_block.timestamp) and (self.prev_hash == other_block.prev_hash) and (self.hash == other_block.hash) and (self.data == other_block.data) and (self.nonce == other_block.nonce) )
    
    # Checks the validity through a proof of work system. If the number of zeros equals the expected number of zeros, it is valid.
    def is_valid(self, chain):
        self.hash = self.hash_generator()
        if(str(self.hash[0:chain.zeroes]) == '0'*chain.zeroes):
            return True
        else:
            return False

