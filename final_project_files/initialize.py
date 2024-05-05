import os
from blockchain import Blockchain
from my_block import Block
import datetime
from mining import mine



def create_genesis_block(chain):
    index = 0
    timestamp = datetime.datetime.now()
    prev_hash = '0' #arbitrary
    data = 'First Block'
    nonce = 0

    first_block = Block(index, timestamp, prev_hash, data, nonce)

    while(str(first_block.hash[0:chain.zeroes])) != '0'* chain.zeroes:
        nonce = nonce+1
        first_block = Block(index,timestamp,prev_hash,data,nonce)
    #print(data)
    return first_block

def initialize_blockchain(node_id):
    chaindata_dir = 'chaindata%s/' % (node_id)
    #print(chaindata_dir)
    new_chain = Blockchain([])

    if not os.path.exists(chaindata_dir):
        os.mkdir(chaindata_dir)
    if os.listdir(chaindata_dir)==[]:
        first_block = create_genesis_block(new_chain)
        new_chain.blocks.append(first_block)
        #new_chain.self_save()
        print(first_block)
        block_one = mine(new_chain)
        new_chain.blocks.append(block_one)
        #new_chain.self_save()
        block_two = mine(new_chain)
        new_chain.blocks.append(block_two)
        #new_chain.self_save()
        #print(new_chain)

    return new_chain