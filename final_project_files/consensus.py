from blockchain import Blockchain
from my_block import Block

# The purpose of this block is to figure out which node on the network has the best
# chain and should be the primary chain. A more sophisticated approach might be used
# in reality and it's possible that not all nodes would always be in contact however
# this should be a realistic approximation.

#each node should have a copy of the network

def find_best_chain(peers):

    if(len(peers)==0):
        print("There currently aren't any nodes in the network!")
        return Blockchain([])
    
    i = 0

    #The purpose of the below loop is to initialize best chain by searching for any valid chain in the network

    while(i < len(peers)):
        if(peers[i].blockchain.is_valid()):
            bestchain = peers[i].blockchain
            break
        else:
            print("Node %s is not using a valid blockchain!" % (peers[i].node_id))
            i = i+1
    
    if(i >= len(peers)):
        print("There are no valid chains in this network.")
        return Blockchain([])


    # The purpose of the below loop is to find the actual best chain within the network. The consensus criteria we're
    # looking for in this case is just that the chain is valid and it is longer than our current best chain. In reality,
    # this would be a more complicated process

    for node in peers:
        if(node.blockchain.is_valid() and len(node.blockchain.blocks) > len(bestchain.blocks)):
            bestchain = node.blockchain
    
    return bestchain
    

        
