#!/usr/bin/python

import time
import hmac
import hashlib
import requests, json


bitso_key = "GQQuvxpTRp"
bitso_secret = "298b382d6ae76792634925aba516599b"
nonce =  str(int(round(time.time() * 1000)))
http_method = "GET"
request_path = "/v3/ledger/"+"?limit=20"
json_payload = ""
# Create signature
message = nonce+http_method+request_path+json_payload

signature = hmac.new(bitso_secret.encode('utf-8'),
                                            message.encode('utf-8'),
                                            hashlib.sha256).hexdigest()

# Build the auth header
auth_header = 'Bitso %s:%s:%s' % (bitso_key, nonce, signature)
# Send request
print request_path
response = requests.get("https://api.bitso.com"+request_path, headers={"Authorization": auth_header} )

print response.content