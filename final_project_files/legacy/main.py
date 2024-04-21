import hashlib
import json
import os
import datetime
import Flask


def create_genesis():
    return Block(0, datetime.datetime(), [], "0")

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

    if __name__ == '__main__':
        chaindata_dir = 'chaindata/'
        if not os.path.exists(chaindata_dir):
            os.mkdir(chaindata_dir)
        if os.listdir(chaindata_dir) == []:
            first_block = create_genesis()
            first_block.self_save()

def sync():
    chain = []
    chaindata_dir = 'chaindata'
    if os.path.exists(chaindata_dir):
        for filename in os.listdir(chaindata_dir):
            if filename.endswith('.json'):
                filepath = '%s/%s' % (chaindata_dir, filename)
                with open(filepath, 'r') as block_file:
                    block_info = json.load(block_file)
                    block_object = Block(block_info)
                    chain.append(block_object)
    return chain

class Blockchain:
    def __init__(self):
        self.chain = [create_genesis()]
    
    def add_block(self, new_block):
        new_block.prev_hash = self.get_last_block().hash
        new_block.hash = new_block.hash_generator(new_block.transactions)
        self.chain.append(new_block)

def displaychain():
    node_blocks = sync()
    python_blocks = []
    for block in node_blocks:
        block_index = str(block.index)
        block_timestamp = str(block.timestamp)
        block_data = str(block.data)
        block_hash = str(block.hash)
        block = { "index": block.index, "timestamp": block.timestamp, "transactions":block.transactions,"hash":block.hash,"prev_hash":block.prev_hash}
        python_blocks.append(block)
    
    json_blocks = json.dumps(python_blocks)
    return json_blocks

node = Flask(__name__)
chain = sync()

@node.route('/blockchain.json', methods=['GET'])

if __name__ == '__main__':
    node.run()
    chain = sync()
    prev_block = chain[-1]
    new_block = mine(prev)



# Below is a test implementation
        
blockchain = Blockchain()
blockchain.add_block(Block(1, datetime.datetime(),[{"sender": "Alice", "recipient": "Bob", "amount": 10}], blockchain.get_last_block().hash))
blockchain.add_block(Block(2, datetime.datetime(),[{"sender": "Bob", "recipient": "Charlie", "amount": 2}], blockchain.get_last_block().hash))

for block in blockchain.chain:
    print("Block #: {}".format(block.index))
    print("TImestamp: {}".format(block.timestamp)) #leaving time as is because otherwise no values will be unique. Alternative idea was to swap to an HH:MM.SS style format.
    print("Transaction Data: {}".format(block.transactions))
    print("Previous Hash: {}".format(block.prev_hash))
    print("Hash: {}\n".format(block.hash))

