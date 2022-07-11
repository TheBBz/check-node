import sys
from tabnanny import check
from urllib import response
import requests
import json
import click
import time
from urllist import URL_LIST
from solana.rpc.api import Client
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware


@click.command()
@click.option(
    "--node_id",
    "-n",
    prompt="Please enter the node id",
    required=True,
    help="Enter the node id",
)
@click.option(
    "--authkey",
    "-a",
    prompt="Please enter authkey",
    required=True,
    hide_input=True,
    help="Enter the node authkey",
)
@click.option(
    "--blockchain",
    "-b",
    prompt="Please enter the blockchain (eth, bsc, polygon, fantom, avax, solana)",
    required=True,
    help="Enter the blockchain type",
)
def check_node(node_id, authkey, blockchain):
    """Blockchain Node Checker, enter the node id and the authentication key and will automatically check if node is synced and compare it with the explorer of the blockchain"""

    if not isinstance(node_id, str):
        return False

    if blockchain == "solana":

        http_client = Client(f"https://{node_id}.p2pify.com/{authkey}")
        response = http_client.get_recent_blockhash()
        solana_latestblock_node = response["result"]["context"]["slot"]
        http_client.get_block_height()

    try:
        w3 = Web3(HTTPProvider(f"https://{node_id}.p2pify.com/{authkey}"))
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    except Exception as e:
        return f"Error: {str(e)}"

    url = URL_LIST[blockchain]["url"]
    payload = URL_LIST[blockchain]["payload"]

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
            print(
                f"\n {blockchain} node id:{node_id} {position} with explorer: {latest_block_node_number}"
            )
        else:
            print(
                f"\n {blockchain} node id:{node_id} {position} of the explorer by {str(diff)} blocks"
            )

        return w3.eth.syncing

    else:
        response = requests.get(url, json=payload)
        solscan_current_slot = response.json()[0]["currentSlot"]
        print(f"\n Solscan current slot is: {solscan_current_slot}")
        print(f"\n Chainstack Node current slot is: {solana_latestblock_node}")


if __name__ == "__main__":
    check_node()
