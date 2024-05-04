from blockchain import Blockchain
from initialize import *
from consensus import *
import json


class Node:
    def __init__(self, node_id, peers = []):
        self.node_id = node_id
        self.peers = peers
        #peers are other nodes directly connected to this one
        self.blockchain = self.sync()

    def add_peer(self,peer):
        self.peers.append(peer)
    
    def receive_chain(self, chain):
        if(chain.is_valid() and len(chain.blocks) > len(self.blockchain.blocks)):
            self.blockchain = chain
            self.chain_save(self.blockchain)
        return
    
    def broadcast_chain(self):

        for peer in self.peers:
            peer.receive_chain(self.blockchain)
        return
    
    def block_save(self,block): #saves the block state locally to the node
        chaindata_dir = 'chaindata%s' % (self.node_id)
        index_string = str(block.index).zfill(6) #adds leading 0s to the filename
        filename = '%s/%s.json' % (chaindata_dir, index_string)

        #Adding this in to allow potential corruption of data

        if(os.path.exists(filename)):
            os.remove(filename)

        with open(filename, 'w') as block_file:
            json.dump({"index":block.index,"timestamp":str(block.timestamp),"data":block.data,"nonce":block.nonce,"hash":block.hash,"prev_hash":block.prev_hash}, block_file)

    def chain_save(self, chain):
        for block in chain.blocks:
            self.block_save(block)

    def sync(self):
    
        chain = Blockchain([])
        chaindata_dir = 'chaindata%s' % (self.node_id)

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
                        chain.blocks.append(block_object)
        
        # if the chaindata directory does not exist for this node, ask for a copy from peers

        else:
            os.mkdir(chaindata_dir)
            chain = find_best_chain(self.peers)
            if(chain.blocks == []):
                chain = initialize_blockchain(self.node_id)
                self.chain_save(chain)
            else:
                self.chain_save(chain)

        return chain