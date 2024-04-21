from blockchain import Blockchain
from my_block import Block

# The purpose of this block is to figure out which node on the network has the best
# chain and should be the primary chain. A more sophisticated approach might be used
# in reality and it's possible that not all nodes would always be in contact however
# this should be a realistic approximation.

#each node should have a copy of the network

def find_best_chain(network):

    if(len(network)==0):
        print("There aren't any nodes in the network!")
        return
    
    i = 0

    #The purpose of the below loop is to initialize best chain by searching for any valid chain in the network

    while(i < len(network)):
        if(network[i].chain.is_valid()):
            bestchain = network[i].chain
            break
        else:
            i = i+1
    
    if(i >= len(network)):
        print("There are no valid chains in this network.")
        return


    # The purpose of the below loop is to find the actual best chain within the network. The consensus criteria we're
    # looking for in this case is just that the chain is valid and it is longer than our current best chain. In reality,
    # this would be a more complicated process

    for node in network:
        if(node.chain.is_valid() and len(node.chain) > len(bestchain)):
            bestchain = node.chain
    
    # This goes back through and sets each node's chain in the network to the best chain that we've previously determined

    for node in network:
        node.chain = bestchain
    

        
