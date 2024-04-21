<h1>Blockchain Overall </h1>

A node is any device that participates in a blockchain. A node will run a blockchain's softwareand allow it to help validate transactions. Having a large number of nodes increases how decentralized a blockchain is and helps keep the network secure by having more actors checking the blockchain's data. Many blockchains will allow anyone to set up a node.

A nonce is used in blockchains designed around the "proof of work" concept. The nonce (which stands for "number only used once") is a pseudorandom number that bitcoin miners attempt to find as part of mining a new block. Miners will perform a brute force attempt to find the correct nonce by repeatedly hashing the block header using different nonce values until the valid hash is confirmed. Each nonce is used only once per block and this is useful for keeping the network secure.

<h1> Block Object </h1>

Each block accepts the following values:
    <ul>
        <li>index: The order this block comes in our chain
        <li>timestamp: When the hash was generated for this block (ie., when this block was created)
        <li>transactions: The data that this block contains. This may be evidence of a bitcoin transaction, or it may be some other type of specific information for this block.
        <li>hash: The unique string specific to this block. This hash value was generated on creation of the block using the data contained within the transactions entry.
        <li>prev_hash: The hash of the previous block in the block chain. By maintaining a record of its own hash and the hash in the preceding block a blockchain can verify that data within the chain has not been modified.
    </ul>

The following methods are used by our Block object:
    <ul>
        <li>self_save: This function is used to save block data locally just in case the node is turned off. The saving here is based on the index, for a larger blockchain this might not be a factor however here if we create a blockchain / block within that blockchain we expect the data to remain the same. </li>
        <li> hash_generator: This function is used to create a hash value for each block that is created. This function uses the hashlib library and the Secure Hash Algorithm (SHA) 256 algorithm. SHA-256 is one of the most commonly used hashing algorithms for blockchains, including Bitcoin.
    </ul>

<h1>Other Functions</h1>
    <ul>
        <li> sync: The sync function is necessary to have the node to update its information on the blockchain. For the purposes of this project, this just means that we're checking the local files to see if anything has been saved when the node previously shutdown. In an actual enterprise blockchain, however, this would include updatingthe blockchain based on transactions that have taken place since the node was previously online. These updates would come form other nodes which have been maintaining a record of the block chain. 