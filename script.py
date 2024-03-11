import json
import os
from web3 import Web3

# Connect to the Infura RPC URL
web3 = Web3(Web3.HTTPProvider('https://eth-mainnet.g.alchemy.com/v2/'))

# Initialize variables
start_block = 1
end_block = 2
blocks_folder = 'blocks'
# Create a directory for the block JSON files
os.makedirs(blocks_folder, exist_ok=True)

# Retrieve all blocks and store them as separate JSON files

while end_block <= web3.eth.block_number:
    blocks = []
    for i in range(start_block, end_block + 1):
        block = web3.eth.get_block(i)
        
        blocks.append(block)

    block_filename = os.path.join(blocks_folder, f'block_{start_block}_to_{end_block}.json')
    with open(block_filename, 'w') as block_file:
        json.dump(blocks, block_file, indent=4)

    # Print a confirmation message after every 100 blocks
    print(f"Blocks {start_block} to {end_block} processed.")

    # Update the start and end block numbers for the next interval
    start_block = end_block + 1
    end_block = start_block + 2


# Store the last processed block number in a separate file
with open('last_processed_block.txt', 'w') as last_block_file:
    last_block_file.write(str(end_block))
