class Blockchain(object):

    def __init__(self,blocks):
        self.blocks = blocks
        self.zeroes = 5 #just selecting this for now, in bitcoin's process PoW difficulty adjusts as needed to keep the average blocks mined from fluctuating too much

    def is_valid(self):

        if(len(self.blocks) == 0):
            print("This blockchain is empty.")
            return True #an empty chain isn't invalid
        else:
            if(not self.blocks[0].is_valid(self)):
                print("Is the genesis block valid?")
                print("No.")
                return False
            prev = self.blocks[0]
            for i, block in enumerate(self.blocks[1:]):
                curr = block

                print("Does %s follow %s?" % (curr.index, prev.index))
                if( (prev.index+1) != (curr.index) ):
                    #print("Previous:", prev)
                    #print("Current:", curr)
                    print("No.")
                    return False # index is out out order, invalid
                print("Yes.")
                print("Does the prev_hash value (%s) stored in the current block ACTUALLY match the previous hash (%s)?" % (curr.prev_hash, prev.hash))
                if( prev.hash != curr.prev_hash):
                    #print("Previous:", prev)
                    #print("Current:", curr)
                    print("No.")
                    return False #think this and the index above should replace the timestamp logic
                print("Yes.")
                print("Does the hash value match our proof of work concept?")
                if( not curr.is_valid(self)):
                    print(curr.hash)
                    print("No.")
                    return False # something is wrong with the hash
                print("Yes.")
                prev = curr
                #Believe this is redundant, the current block having the previous block's hash should be enough to 
                #indicate that the previous block came before the current block

                #if( (prev.timestamp) > (curr.timestamp) ): 
                #    return False # previous block came before current block.
            print("The blockchain has been validated.")
            return True

    def get_last_block(self):
        return self.blocks[-1]
    
    def print_blockchain_basic(self):

        for i, block in enumerate(self.blocks):
            print("Block #%s, Data: %s , hash: %s" % (block.index, block.data, block.hash))

    def find_by_index(self,search_index):

        for i, block in enumerate(self.blocks):
            #print(block.index)
            if(block.index == int(search_index)):
                return block
        
        print("Block index not found.")
        return
    
    def add_block(self,block):
        self.blocks.append(block)
        return

    
    #copies the self-save logic to create a copy of the whole chain locally
    # def self_save(self):
    #     for block in self.blocks:
    #         block.self_save()
                
            