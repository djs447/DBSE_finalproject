# Blockchain Requirements Document

The requirements outlined in this document will be used to define the necessary functions of a blockchain ledger to work effectively. These requirements are being defined as laid out in Satoshi Nakamoto's whitepaper on Bitcoin, titled *Bitcoin: A Peer-to-Peer Electronic Cash System*. While Bitcoin is not representative for all blockchain ledger structures, this provides a detailed schematic for one possible blockchain implementation. Where possible I'll try to explain how different blockchain implementations might differ from this one however the objective of this project will include using the Bitcoin structure as a technical benchmark.

## Block

A block is a set of items which is hashed, along with a timestamp, and widely published to all other nodes within a network.

#### Contents

* Each block shall contain the timestamp, the hash of the previous block, and data relating to the transaction.
    * The block shall contain an index giving it's position within the chain. *Derived requirement: While not explicitly stated in the bitcoin whitepaper, I'm adding this in to make it easier to track / debug values.*
* All of the contents of a block shall be used to generate the hash of that block.
* The SHA-256 algorithm shall be used to generate the hash value for each block.
* The nonce value shall be used to establish a Proof-of-Work system. When hashed, the hash can be verified if it begins with the required number of zero bits.
    * Once a satisfactory hash has been reached according to the proof-of-work principle, the block cannot be changed without redoing the work and changing all following blocks.
* The nonce value within a block shall be incremented until a value is found that gives the block's hash the required number of zero bits.

#### Validity

* Blocks shall satisfy the following criteria in order to be valid:
    1. The block shall have the required (expected) number of zero bits as prescribed by the blockchain
    2. The previous block hash value stored within the current block shall match the actual hash value of the previous block.
    3. The blocks within the blockchain shall be connected in the order they were mined.


## Node

A node is essentially a computer which participates in Bitcoin's network. Nodes must communicate with each other to keep track of the blockchain and update each other with any new transactions.

* New transactions shall be broadcast to all nodes.
    * *Bitcoin uses a 

* Each node shall collect new transactions into a block

* When a node find a proof-of-work, it shall broadcast the block to all nodes.

* Nodes shall accept the block only if all transactions in it are valid and not already spent.
    * *Aside, in my implementation I need to double-check to make sure that my transactions aren't "spent" (transactions are unique in this case?)*

* Nodes shall express their acceptance of the block by working on creating the next block in the chain, using the hash of the accepted block as the previous hash.

* Nodes shall utilize a method for reaching consensus, such that all nodes can agree on a single chain.
    * *Bitcoin has it's own procedures for settling ties, where each node tracks alternative "branches" until a consensus can be reached. There might be a simpler way to implement this since we're likely only going to be looking at smaller networks for this project.*




## Blockchain

An electronic coin is a chain of digital signatures, where each owner transfers the coin to the next owner by digitally signing a hash of the previous transaction and the public key of the next owner and adding these to the end of the coin. The longest chain reperesents the majority decision of all nodes, since the longest chain has the most work put into it.

* The blockchain shall specify the expected number of zeroes to adhere to the Proof-of-Work principle.
    * *Derived requirement: This isn't specified by the bitcoin whitepaper however for the sake of implementation this will make it easier to track how many zeroes are necessary. In reality it there's a global mining difficulty, keeping in the spirit of this assumption, however this difficulty is adjusted over time to be harder/easier to meet a moving average targeting a specific "average number of blocks per hour". For the sake of this project, the number of zeroes shall be left as a static integer* 

#### Validity

* The recipient of a coin shall be able to verify the chain of ownership by verifying the chain of signatures.

* Transactions shall be publicly distributed to all nodes participating within the network.

* The validity of a blockchain shall require each of the blocks it contains to be valid.



