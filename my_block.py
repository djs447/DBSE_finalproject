import hashlib
import os
import json
import datetime

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

        with open(filename, 'w') as block_file:
            json.dump({"index":self.index,"timestamp":str(self.timestamp),"data":self.data,"nonce":self.nonce,"hash":self.hash,"prev_hash":self.prev_hash}, block_file)

    def __init__(self, index, timestamp, prev_hash, data, nonce, hash = None):
        self.index = index
        self.timestamp = timestamp
        self.prev_hash = prev_hash
        self.data = data
        self.nonce = nonce #set this randomly? something to come back to
        
        #Differentiates when a new block is created or not
        if hash is not None:
            self.hash = hash
        else:
            self.hash = self.hash_generator()

        #print(self.hash)


def create_genesis_block():
    index = 0
    timestamp = datetime.datetime.now()
    prev_hash = '0' #arbitrary
    data = 'First Block'
    nonce = 0 #arbitrary
    #print(data)
    return Block(index, timestamp, prev_hash, data, nonce)

if __name__ == '__main__':
    chaindata_dir = 'chaindata/'
    #print(chaindata_dir)

    if not os.path.exists(chaindata_dir):
        os.mkdir(chaindata_dir)
    if os.listdir(chaindata_dir)==[]:
        #print("Flippy Flappy")
        first_block = create_genesis_block()
        #print(first_block)
        first_block.self_save()
        #print(first_block)

