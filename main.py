import sys
import requests
import json
from solana.rpc.api import Client
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware

# from settings import API_KEY


def check_node(node_url, blockchain):
    if not isinstance(node_url, str):
        return False

    url_lists = {
        "eth": {
            "url": "https://api.etherscan.io/api?module=proxy&action=eth_blockNumber&apikey=YourApiKeyToken",
            "payload": {
                "method": "echo",
                "params": ["echome!"],
                "jsonrpc": "2.0",
                "id": 0,
            },
        },
        "bsc": {
            "url": "https://api.bscscan.com/api?module=proxy&action=eth_blockNumber&apikey=YourApiKeyToken",
            "payload": {
                "method": "echo",
                "params": ["echome!"],
                "jsonrpc": "2.0",
                "id": 0,
            },
        },
        "polygon": {
            "url": "https://api.polygonscan.com/api?module=proxy&action=eth_blockNumber&apikey=YourApiKeyToken",
            "payload": {
                "method": "echo",
                "params": ["echome!"],
                "jsonrpc": "2.0",
                "id": 0,
            },
        },
        "fantom": {
            "url": "https://api.ftmscan.com/api?module=proxy&action=eth_blockNumber&apikey=YourApiKeyToken",
            "payload": {
                "method": "echo",
                "params": ["echome!"],
                "jsonrpc": "2.0",
                "id": 0,
            },
        },
        "avax": {
            "url": "https://api.snowtrace.io/api?module=proxy&action=eth_blockNumber&apikey=YourApiKeyToken",
            "payload": {
                "method": "echo",
                "params": ["echome!"],
                "jsonrpc": "2.0",
                "id": 0,
            },
        },
        "solana": {
            "url": "https://public-api.solscan.io/block/last?limit=1",
            "payload": {},
        },
    }

    if blockchain == "solana":

        http_client = Client(node_url)
        response = http_client.get_recent_blockhash()
        solana_latestblock_node = response["result"]["context"]["slot"]
        http_client.get_block_height()

    try:
        w3 = Web3(HTTPProvider(node_url))
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    except Exception as e:
        return f"Error: {str(e)}"

    url = url_lists[blockchain]["url"]
    # print("url in use: " , url)
    payload = url_lists[blockchain]["payload"]

    if blockchain != "solana":
        response = requests.post(url, json=payload).json()
        etherscan = int(response["result"], 0)
        # etherscan16 = (int(response["result"], 16))
        diff = w3.eth.block_number - etherscan
        latest_block_node_number = None

        if w3.eth.block_number > etherscan:
            position = "is ahead"
        elif w3.eth.block_number < etherscan:
            position = "is behind"
        else:
            position = "is synced"
            latest_block_node_number = w3.eth.block_number

        if position == "is synced" and latest_block_node_number:
            print(f"Node {position} with explorer: {latest_block_node_number}")
        else:
            print(f"Node {position} of explorer by {str(diff)} blocks")

        return w3.eth.syncing

    else:
        response = requests.get(url, json=payload)
        solscan_current_slot = response.json()[0]["currentSlot"]
        print(f"Solscan current slot is: {solscan_current_slot}")
        print(f"Chainstack Node current slot is: {solana_latestblock_node}")


if __name__ == "__main__":
    check_node(sys.argv[1], sys.argv[2])
