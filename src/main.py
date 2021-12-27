from Block.block import block

myblock: block = block('abc', ['abd', 'dcda'])

print(myblock.get_block_hash().hexdigest())