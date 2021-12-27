from BlockChain.Block.block import Block

myblock: Block = Block('abc', ['abd', 'dcda'])

print(myblock.get_block_hash().hexdigest())