import json
import requests
from solana.rpc.api import Client
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware


def check_node(node_id, authmethod, blockchain):
    """Blockchain Node Checker, enter the node id and the authentication key and will automatically check if node is synced and compare it with the explorer of the blockchain"""


node_id = input("Enter the node id:")
authmethod = input("Enter the authorization method (for Key auth type 'k' for basic auth type 'b'):")
if authmethod == "k":
    authkey = input("Enther the Key auth:")
if authmethod == "b":
    basicmethod = input("Enter the user and password:")

blockchain = input("Enter the blockchain (eth, bsc, polygon, fantom, avax, solana):")

with open("list.json") as jsonlist:
    list = json.load(jsonlist)
url = list[blockchain]["url"]
payload = list[blockchain]["payload"]

if blockchain == "Solana":
    """This block is to connect to Solana RPC Node"""
    if authmethod == "k":
        http_client = Client(f"https://{node_id}.p2pify.com/{authkey}")
    if authmethod == "b":
        http_client = Client(f"https://{basicmethod}@{node_id}.p2pify.com")
        try:
            response = http_client.get_recent_blockhash()
            solana_latestblock_node = response["result"]["context"]["slot"]
        # http_client.get_block_height()
        except Exception as e:
            print(e.message)


        """This block compares the Solana RPC node latest block with the blockchain explorer latest block"""
        api_response = requests.get(url, json=payload)
        solscan_current_slot = api_response.json()[0]["currentSlot"]
        print(f"Solscan current slot is: {solscan_current_slot}")
        print(f"Chainstack Node current slot is: {solana_latestblock_node}")

if blockchain != "Solana":
    """This block is to connect to a EVM RPC Node"""
    if authmethod == "k":
        w3 = Web3(HTTPProvider(f"https://{node_id}.p2pify.com/{authkey}"))
    if authmethod == "b":
        w3 = Web3(HTTPProvider(f"https://{basicmethod}@{node_id}.p2pify.com"))
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        response = requests.post(url, json=payload).json()
        etherscan = int(response["result"], 0)
        # etherscan16 = (int(response["result"], 16))
        diff = w3.eth.block_number - etherscan
        latest_block_node_number = None



    if w3.eth.block_number > etherscan:
        """This block compares the EVM RPC node latest block with the blockchain explorer latest block"""
        position = "is ahead"
    elif w3.eth.block_number < etherscan:
        position = "is behind"
    else:
        position = "is synced"
        latest_block_node_number = w3.eth.block_number

    if position == "is synced" and latest_block_node_number:
        print(
            f"\n {blockchain} node id: {node_id} {position} with explorer: {latest_block_node_number}"
        )
    else:
        print(
            f"\n {blockchain} node id: {node_id} {position} of the explorer by {str(diff)} blocks"
        )


# try:
#    check_node()
# except Exception as e:
#    print(e.message)