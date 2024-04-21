from my_block import Block
from blockchain import Blockchain
import datetime
import my_sync


def mine(chain):
    
    #Define the new block parameters

    last = chain.get_last_block()

    index = int(last.index) +1
    timestamp = datetime.datetime.now()
    data = "This is block #%s" % (index) #This data is a placeholder and should be replaced with an actual string
    prev_hash = last.hash
    nonce = 0
    
    newblock = Block(index, timestamp, prev_hash, data, nonce)

    #This while-loop retrieves the first few characters of the hash value. The use of nonce here
    #forces an extra step in the hash generation process to slow it down. This while loop terminates
    #if the beginning substring of zeros is the same as the number of zeros specified in the 'zeros'
    #variable

    while str(newblock.hash[0:chain.zeroes]) != '0' * chain.zeroes: 
        nonce = nonce + 1
        newblock = Block(index, timestamp, prev_hash, data, nonce)

    return newblock

def mining_input(chain):
    
    #Define the new block parameters

    last = chain.get_last_block()

    index = int(last.index) +1
    timestamp = datetime.datetime.now()
    data = input("Enter the info you want to store in the blockchain:\n") #This data is anything you want to keep secure
    prev_hash = last.hash
    nonce = 0
    
    newblock = Block(index, timestamp, prev_hash, data, nonce)

    #This while-loop retrieves the first few characters of the hash value. The use of nonce here
    #forces an extra step in the hash generation process to slow it down. This while loop terminates
    #if the beginning substring of zeros is the same as the number of zeros specified in the 'zeros'
    #variable

    start_time = datetime.datetime.now()
    attempts = 0
    while str(newblock.hash[0:chain.zeroes]) != '0' * chain.zeroes: 
        nonce = nonce + 1
        newblock = Block(index, timestamp, prev_hash, data, nonce)
        attempts = attempts+1
    
    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time
    print("Time to Mine: %s seconds. Total attempts: %s ." % (elapsed_time, attempts))

    return newblock


if __name__ == '__main__':
    chain = my_sync.sync()
    new_block = mine(chain)
    new_block.self_save()