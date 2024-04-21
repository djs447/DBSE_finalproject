from blockchain import Blockchain
from my_block import Block
from my_sync import sync
from mining import mining_input
import time

import argparse

# def get_command():
#     parser = argparse.ArgumentParser(description="Enter the function you want to demo, 'validity', ")
#     parser.add_argument('demo_command', type=str)
#     args = parser.parse_args()
#     return args.demo_command

def validity_demo():
    chain = sync()
    #print("this is my chain", chain)
    chain.is_valid()
    return

def mining_demo():
    chain = sync()
    print("Original Blockchain")
    chain.print_blockchain_basic()

    new_block = mining_input(chain)
    new_block.self_save()

    chain = sync()

    print("\nUpdated Blockchain")
    chain.print_blockchain_basic()
    return

def corrupt_demo():
    chain = sync()
    print("Original Blockchain")
    chain.print_blockchain_basic()

    index = input("Enter the index of the block you want to break:\n")
    new_data = input("Enter the new data you want to insert:\n")

    broken_block = chain.find_by_index(index)
    broken_block.data = new_data
    broken_block.self_save()

    #chain = sync()

    print("Updated Block")
    chain.print_blockchain_basic()
    return

def print_chain():
    chain = sync()
    print("Current Blockchain Status:")
    chain.print_blockchain_basic()
    return

if __name__ == "__main__":
        
    while(True):
        command = input("Enter the function you want to demo: (validity), (mine), (theft), (print) or (end) if you're done\n")

        if(command == 'end'):
            print('Demo ending.')
            break
        elif(command == 'validity'):
            validity_demo()
        elif(command == 'mine'):
            mining_demo()
        elif(command == 'theft'):
            corrupt_demo()
        elif(command == 'print'):
            print_chain()
        else:
            print("Invalid command: Please try again.")
    
