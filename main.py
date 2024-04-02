import hashlib
import time
import json
import os


class Block:
    def __init__(self, index, timestamp, transactions, prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.hash = self.hash_generator(transactions)
        self.prev_hash = prev_hash

    def hash_generator(self, transactions):
        result = hashlib.sha256(json.dumps(transactions).encode()) #The json.dumps() function is necessary to convert a Python object into a JSON formatted string, and then run encode
        return result.hexdigest()
    
    def self_save(self):
        chaindata_dir = 'chaindata'
        index_string = str(self.index).zfill(6) #Leading zeros keeps blocks in order
        filename = '%s/%s.json' % (chaindata_dir, index_string)
        with open(filename, 'w') as block_file:
            json.dump({"index":self.index,"timestamp":self.timestamp,"transactions":self.transactions,"hash":self.hash,"prev_hash":self.prev_hash}, block_file) #might run into trouble with this implementation, possibly better to dump as dictionary


def create_genesis():
    return Block(0, time.time(), [], "0")

class Blockchain:
    def __init__(self):
        self.chain = [create_genesis()]
    
    if __name__ == '__main__': #saves data in the 'chaindata' directory
        chaindata_dir = 'chaindata/'
        if not os.path.exists(chaindata_dir):
            os.mkdir(chaindata_dir)
        if os.listdir(chaindata_dir) == []:
            first_block = create_genesis()
            first_block.self_save()
    
    def get_last_block(self):
        return self.chain[-1]
    
    def add_block(self, new_block):
        new_block.prev_hash = self.get_last_block().hash
        new_block.hash = new_block.hash_generator(new_block.transactions)
        self.chain.append(new_block)

# Below is a test implementation
        
blockchain = Blockchain()
blockchain.add_block(Block(1, time.time(),[{"sender": "Alice", "recipient": "Bob", "amount": 10}], blockchain.get_last_block().hash))
blockchain.add_block(Block(2, time.time(),[{"sender": "Bob", "recipient": "Charlie", "amount": 2}], blockchain.get_last_block().hash))

for block in blockchain.chain:
    print("Block #: {}".format(block.index))
    print("TImestamp: {}".format(block.timestamp)) #leaving time as is because otherwise no values will be unique. Alternative idea was to swap to an HH:MM.SS style format.
    print("Transaction Data: {}".format(block.transactions))
    print("Previous Hash: {}".format(block.prev_hash))
    print("Hash: {}\n".format(block.hash))

