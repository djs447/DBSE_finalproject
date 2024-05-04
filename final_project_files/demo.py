from blockchain import Blockchain
from my_block import Block
from mining import mining_input
import time
import backup
from node import *

import argparse

# def get_command():
#     parser = argparse.ArgumentParser(description="Enter the function you want to demo, 'validity', ")
#     parser.add_argument('demo_command', type=str)
#     args = parser.parse_args()
#     return args.demo_command

def validity_demo(node):
    chain = node.sync()
    #print("this is my chain", chain)
    chain.is_valid()
    return

def mining_demo(node):
    chain = node.sync()
    print("Original Blockchain")
    chain.print_blockchain_basic()

    new_block = mining_input(chain)
    chain.add_block(new_block)
    node.chain_save(chain)

    #chain = node.sync()

    print("\nUpdated Blockchain")
    chain.print_blockchain_basic()
    return

def corrupt_demo(node):
    chain = node.sync()
    print("Original Blockchain")
    chain.print_blockchain_basic()
    
    while(True):
        index = int(input("Enter the index of the block you want to break:\n"))
        if index in range(0, len(chain.blocks),1):
            break
        else:
            print("Invalid Entry, try again.")
            #print(range(0, len(chain.blocks),1))

    new_data = input("Enter the new data you want to insert:\n")

    broken_block = chain.find_by_index(index)
    broken_block.data = new_data
    node.chain_save(chain)

    #chain = sync()

    print("Updated Block")
    chain.print_blockchain_basic()
    return

def print_chain(node):
    chain = node.sync()
    print("Current Blockchain Status:")
    chain.print_blockchain_basic()
    return

def consensus_demo(node):
    network = node.peers
    bestchain = find_best_chain(network)

    if( (len(node.blockchain.blocks) < len(bestchain.blocks) ) or (not node.blockchain.is_valid())):
        node.blockchain = bestchain
        node.chain_save(node.blockchain)
    node.broadcast_chain()

    return


if __name__ == "__main__":

    zero_node = Node(0)
    #Note: One Node will not automically receive the longest chain upon start up of the program, it will need to be shared
    one_node = Node(1,[zero_node])

    zero_node.add_peer(one_node)
    
    print_chain(zero_node)
        
    while(True):
        command = input("Enter the function you want to demo for the 0th node: (validity), (mine), (theft), (print), (store), (load), (consensus), or (end) if you're done\n")

        if(command == 'end'):
            print('Demo ending.')
            break
        elif(command == 'validity'):
            validity_demo(zero_node)
        elif(command == 'mine'):
            mining_demo(zero_node)
        elif(command == 'theft'):
            corrupt_demo(zero_node)
        elif(command == 'print'):
            print_chain(zero_node)
        elif(command == 'store'):
            backup.backup_store(zero_node.node_id)
        elif(command == 'load'):
            backup.backup_load(zero_node.node_id)
        elif(command == 'consensus'):
            consensus_demo(zero_node)
        else:
            print("Invalid command: Please try again.")
    
