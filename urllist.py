from cmath import log
from click import echo
from requests import URLRequired

URL_LIST = {
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