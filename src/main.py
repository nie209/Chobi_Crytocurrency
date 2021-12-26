from Block.block import block


myblock: block = block('abc', ['abc', 'dcda'])


print(dir(myblock.get_block_hash()))