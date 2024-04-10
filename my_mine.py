from my_block import Block
import datetime
import my_sync


zeros = 4

def get_last_block(chain):
    return chain[-1]

def mine(last):
    
    #Define the new block parameters

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

    while str(newblock.hash[0:zeros]) != '0' * zeros: 
        nonce = nonce + 1
        newblock = Block(index, timestamp, prev_hash, data, nonce)
        # The way I wrote the above loop is probably a bit slower than just calculating the hash
        # each time since more work will be necessary before nonce is increased

    return newblock


if __name__ == '__main__':
    chain = my_sync.sync()
    last_block = get_last_block(chain)
    new_block = mine(last_block)
    new_block.self_save()