#!/usr/bin/env python3

from black import main
from checknode import check_node
from gettx import get_transaction
import click
import requests


if __name__ == "__main__":
    try:
        check_node()
    except requests.exceptions.HTTPError as e:
        raise Exception("Invalid node id or auth key")
