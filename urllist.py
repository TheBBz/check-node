URL_LIST = {
    "ETH": {
        "url": "https://api.etherscan.io/api?module=proxy&action=eth_blockNumber&apikey=YourApiKeyToken",
        "payload": {
            "method": "echo",
            "params": ["echome!"],
            "jsonrpc": "2.0",
            "id": 0,
        },
    },
    "BSC": {
        "url": "https://api.bscscan.com/api?module=proxy&action=eth_blockNumber&apikey=YourApiKeyToken",
        "payload": {
            "method": "echo",
            "params": ["echome!"],
            "jsonrpc": "2.0",
            "id": 0,
        },
    },
    "Polygon": {
        "url": "https://api.polygonscan.com/api?module=proxy&action=eth_blockNumber&apikey=YourApiKeyToken",
        "payload": {
            "method": "echo",
            "params": ["echome!"],
            "jsonrpc": "2.0",
            "id": 0,
        },
    },
    "Fantom": {
        "url": "https://api.ftmscan.com/api?module=proxy&action=eth_blockNumber&apikey=YourApiKeyToken",
        "payload": {
            "method": "echo",
            "params": ["echome!"],
            "jsonrpc": "2.0",
            "id": 0,
        },
    },
    "Avax": {
        "url": "https://api.snowtrace.io/api?module=proxy&action=eth_blockNumber&apikey=YourApiKeyToken",
        "payload": {
            "method": "echo",
            "params": ["echome!"],
            "jsonrpc": "2.0",
            "id": 0,
        },
    },
    "Solana": {
        "url": "https://public-api.solscan.io/block/last?limit=1",
        "payload": {},
    },
}
