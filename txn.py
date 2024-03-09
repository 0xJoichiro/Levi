from web3 import Web3
import json
from web3.datastructures import AttributeDict

# Connect to the Infura RPC URL
web3 = Web3(Web3.HTTPProvider('https://eth-mainnet.g.alchemy.com/v2/1Fqrvju7DLrHM1TmU2ZvLcZ8cH9X2ph8'))

# 2306
# Initialize variables
start_block = 19392030
end_block = start_block + 10
# end_block = web3.eth.block_number
blocks = {}

# 19392030

for i in range(start_block, end_block):
    print(i,"i block")
    block_data = web3.to_json(web3.eth.get_block(i))
    # print(block_data)
    block = json.loads(block_data)

    print("length",len(block["transactions"]))
    if len(block["transactions"]) > 0:
        for tx_hash in block["transactions"]:
            # print("tx_hash",tx_hash)
            transaction_data = web3.to_json(web3.eth.get_transaction(tx_hash))
            transaction = json.loads(transaction_data)
            # print("transaction ================>",transaction)
            txn_receipt = web3.to_json(web3.eth.get_transaction_receipt(tx_hash))
            transaction_receipt = json.loads(txn_receipt)
            # print("transaction_receipt",transaction_receipt)
            if transaction_receipt['contractAddress'] is not None:
                contract_address = transaction_receipt['contractAddress']
                print('contract_address',contract_address)
                bytecode = web3.eth.get_code(contract_address)
                bytecode_data = {
                    'tx_hash': tx_hash,
                    'contract_address': contract_address,
                    'bytecode': bytecode.hex()
                }
                print("bytecode_data",bytecode_data)

                blocks.setdefault('block_' + str(i), []).append(bytecode_data)
        
 
        
        # if transaction["to"] is None:
        #     # Contract creation transaction
        #     transaction_receipt = web3.to_json(web3.eth.get_transaction_receipt(tx_hash))
        #     print("get_transaction_receipt",transaction_receipt)

        #     print("transaction ================>",transaction)
        #     print(transaction["to"],"transaction.to")
        #     print(transaction["contractAddress"],"======================== transaction.contractAddress")
        #     contract_address = transaction["contractAddress"]
        #     bytecode = web3.eth.get_code(contract_address)
        #     bytecode_data = {
        #         'tx_hash': tx_hash,
        #         'contract_address': contract_address,
        #         'bytecode': bytecode.hex()
        #     }
            
        #     # Store bytecode data in the blocks dictionary
        #     blocks.setdefault('block_' + str(i), []).append(bytecode_data)

# Store the dictionary in a JSON file
with open(f'bytecode_data_{start_block}_{end_block}.json', 'w') as file:
    json.dump(blocks, file, indent=4)







# from web3 import Web3

# # Connect to the Infura RPC URL
# web3 = Web3(Web3.HTTPProvider('https://eth-mainnet.g.alchemy.com/v2/1Fqrvju7DLrHM1TmU2ZvLcZ8cH9X2ph8'))

# # Initialize variables
# start_block = web3.eth.block_number - 1
# end_block = web3.eth.block_number

# for i in range(start_block, end_block + 1):
#     block_hex = web3.to_json(web3.eth.get_block(i, full_transactions=True))
#     print(block_hex)
#     # Convert hexadecimal string to dictionary
    
#     block = web3.eth.from_blob(block_hex)

#     # Iterate through the transactions in the block
#     for tx_hash in block['transactions']:
#         print(tx_hash)
