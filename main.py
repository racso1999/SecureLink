import requests
import os
from dotenv import load_dotenv

from mcp.server.mcpserver import MCPServer

import json

mcp = MCPServer("securelink")

load_dotenv()

BASE_URL = "https://api.starlingbank.com/api/v2"

s = requests.Session()

s.headers["Authorization"] = f"Bearer {os.environ['STARLING_API_KEY']}"

@mcp.tool()
def get_account_information():
    account_information = s.get(f"{BASE_URL}/accounts").json()
    return account_information

@mcp.tool()
def get_accountUid():
    accountUid = s.get(f"{BASE_URL}/accounts").json()['accounts'][0]['accountUid']
    return accountUid

@mcp.tool()
def get_balance():
    accountUid = get_accountUid()
    balance = s.get(f"{BASE_URL}/accounts/{accountUid}/balance").json()
    return balance



if __name__=="__main__":
    mcp.run(transport="streamable-http")