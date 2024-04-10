from my_block import Block

import os
import json

# If a chain has been saved or there have been changes to the blockchain since the
# node went offline this function is to update that. It checks to see if the
# chaindata directory exists, then loads data from each block that has been saved
# and returns this data as a chain of dicts

def sync():
    
    chain = []
    chaindata_dir = 'chaindata'

    if os.path.exists(chaindata_dir):
        for filename in os.listdir(chaindata_dir):
            if filename.endswith('.json'):

                filepath = '%s/%s' % (chaindata_dir, filename)

                with open(filepath, 'r') as block_file:

                    block_info = json.load(block_file)
                    index = block_info["index"]
                    timestamp = block_info["timestamp"]
                    data = block_info["data"]
                    nonce = block_info["nonce"]
                    hash = block_info["hash"]
                    prev_hash = block_info["prev_hash"]
                    block_object = Block(index,timestamp,prev_hash,data,nonce,hash)
                    chain.append(block_object)
    return chain