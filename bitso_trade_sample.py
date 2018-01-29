#!/usr/bin/python

import time
import hmac
import hashlib
import requests, json


bitso_key = "GQQuvxpTRp"
bitso_secret = "298b382d6ae76792634925aba516599b"
nonce =  str(int(round(time.time() * 1000)))
http_method = "POST"
request_path = "/v3/orders/"
json_data_market = "{\"book\":\"eth_btc\",\"side\":\"buy\",\"type\":\"market\",\"minor\":\"0.00001\"}"
json_data_limit = "{\"book\":\"eth_btc\",\"side\":\"buy\",\"type\":\"limit\",\"major\":\"0.00009499\",\"price\":\"0.1035\"}"
json_payload = json_data_limit
print "\njson_payload = "+ json_payload
# Create signature
message = nonce+http_method+request_path+json_payload
print "\nmessage = "+message
signature = hmac.new(bitso_secret.encode('utf-8'),
                                            message.encode('utf-8'),
                                            hashlib.sha256).hexdigest()

# Build the auth header
auth_header = 'Bitso %s:%s:%s' % (bitso_key, nonce, signature)
print "\nauth_header = "+auth_header
# Send request
response = requests.post("https://api.bitso.com"+request_path, data=json_payload, headers={"Authorization": auth_header,'content-type': "application/json"} )

print response.content