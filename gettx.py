from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware


def get_transaction(node_id, authkey, tx):
    """Blockchain transaction getter, enter the node id and the authentication key and will automatically fetch the transaction from the node"""


node_id = input("Enter the node id:")
authkey = input("Enter the authkey:")
tx = input("Enter the transaction hash:")

w3 = Web3(HTTPProvider(f"https://{node_id}.p2pify.com/{authkey}"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
w3.eth.get_transaction(f"{tx}")
print(w3.eth.get_transaction(f"{tx}"))
