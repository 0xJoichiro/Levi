from web3 import Web3
import json
from web3.datastructures import AttributeDict

# Connect to the Infura RPC URL
web3 = Web3(Web3.HTTPProvider('https://eth-mainnet.g.alchemy.com/v2/'))

# Initialize variables
start_block = web3.eth.block_number - 5
end_block = web3.eth.block_number
blocks = {}

for i in range(start_block, end_block + 1):
    block = web3.eth.get_block(i)
    print(web3.to_json(block))
    blocks[i] = web3.to_json(block)




# Store the dictionary in a JSON file
with open('blocks_data.json', 'w') as file:
    json.dump(blocks, file)



ok = web3.eth.get_transaction('0x2710a391a8b79f4ff86ea46be1aebfa061fd806174b3463b72b5509caf0dd8a9')
print(web3.to_json(ok))
