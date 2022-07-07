import sys
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware

from settings import API_KEY


def check_node(node_url):
    if not isinstance(node_url, str):
        return False

    try:
        w3 = Web3(HTTPProvider(node_url))
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    except Exception as e:
        return f"Error: {str(e)}"

    print("Latest block number is", w3.eth.block_number)
    latest_block = w3.eth.get_block("latest")
    return w3.eth.syncing


if __name__ == "__main__":
    check_node(sys.argv[1])
