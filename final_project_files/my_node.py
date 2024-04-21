#from my_block import Block
from flask import Flask
from my_sync import sync

import os
import json

# I'm leveraging some of the code from a similar project here to visualize the blockchain
# as I go, so far I've been using print() statements which have gotten messy. The purpose of
# this is so I can validate the blockchain visually, Flask is just an easy way to show this in browser.

node = Flask(__name__)

chain = sync()

@node.route('/blockchain.json', methods=['GET']) #url is "127.0.0.1:5000/blockchain.json"

def print_blockchain():

    chain = sync()
    print_blocks = []

    for block in chain.blocks:
        print_blocks.append({"index":block.index,"timestamp":str(block.timestamp),"data":block.data,"nonce":block.nonce,"hash":block.hash,"prev_hash":block.prev_hash})

    return json.dumps(print_blocks)

if __name__ == '__main__':
    node.run()