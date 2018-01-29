#BITSO PRIVATE API

from bitso_general_api import *

## Bitso Autorization Headers START
def getAutorizationHeader(http_method, endpoint, json_payload=""):
	nonce = getNonce();
	message = getMessage(nonce, http_method, endpoint, json_payload)
	signature = getSignature(bitso_secret, message)
	auth_header = getAuthHeader(bitso_key, nonce, signature )
	return auth_header

def getAuthorizationHeaderGET(endpoint):
	return getAutorizationHeader("GET", endpoint)

def getAuthorizationHeaderPOST(endpoint, json_payload=""):
	return getAutorizationHeader("POST", endpoint, json_payload)

def getAuthorizationHeaderDELETE(endpoint):
	return getAutorizationHeader("DELETE", endpoint)
## Bitso Autorization Headers END

## Account Status START ##
def account_status():
	endpoint = "/v3/account_status/"
	try:
		auth_header = getAuthorizationHeaderGET(endpoint)
		headers = {"Authorization":auth_header}
		response = getGETRequestHeaders(endpoint,headers)
	except requests.exceptions.RequestException as e:  
		print "Error: " + e
		return {}

	return response.content
## Account Status END ##

## Account Balance START ##
def account_balance():
	endpoint = "/v3/balance/"
	try:
		auth_header = getAuthorizationHeaderGET(endpoint)
		headers = {"Authorization":auth_header}
		response = getGETRequestHeaders(endpoint,headers)
	except requests.exceptions.RequestException as e:  
		print "Error: " + e
		return {}
	return response.content
## Account Balance END ##

## Fees START ##
def fees():
	endpoint = "/v3/fees/"
	try:
		auth_header = getAuthorizationHeaderGET(endpoint)
		headers = {"Authorization":auth_header}
		response = getGETRequestHeaders(endpoint,headers)
	except requests.exceptions.RequestException as e:  
		print "Error: " + e
		return {}
	return response.content
## Fees END ##

## Ledger START ##
def ledger(marker = "", sort ="", limit="", ledger=""):
	endpoint = "/v3/ledger/"
	try:
		params = { "marker":marker, "sort":sort, "limit":limit}
		endpoint += ledger+getQueryParameters(params)
		auth_header = getAuthorizationHeaderGET(endpoint)
		
		headers = {"Authorization":auth_header}
		response = getGETRequestHeaders(endpoint,headers)
	except requests.exceptions.RequestException as e:  
		print "Error: " + e
		return {}
	return response.content
## Ledger END ##

## Withdrawals START ##
## Withdrawals END ##

## Fundings START ##
## Fundings END ##

## User Trades START ##
def user_trades(marker = "", sort ="", limit="", tids=""):
	endpoint = "/v3/user_trades/"
	try:
		params = { "marker":marker, "sort":sort, "limit":limit}
		endpoint += tids+getQueryParameters(params)
		auth_header = getAuthorizationHeaderGET(endpoint)
		
		headers = {"Authorization":auth_header}
		response = getGETRequestHeaders(endpoint,headers)
	except requests.exceptions.RequestException as e:  
		print "Error: " + e
		return {}
	return response.content
## User Trades END ##

## Order Trades START ##
def order_trades( oid=""):
	endpoint = "/v3/order_trades/"
	try:
		endpoint += oid
		auth_header = getAuthorizationHeaderGET(endpoint)
		
		headers = {"Authorization":auth_header}
		response = getGETRequestHeaders(endpoint,headers)
	except requests.exceptions.RequestException as e:  
		print "Error: " + e
		return {}
	return response.content
## Order Trades END ##

## Open Orders START ##
def open_orders(book = "", marker = "", sort ="", limit=""):
	endpoint = "/v3/open_orders/"
	try:
		params = {"book":book, "marker":marker, "sort":sort, "limit":limit}
		endpoint += getQueryParameters(params)
		auth_header = getAuthorizationHeaderGET(endpoint)
		headers = {"Authorization":auth_header}
		response = getGETRequestHeaders(endpoint,headers)
	except requests.exceptions.RequestException as e:  
		print "Error: " + e
		return {}
	return response.content
## Open Orders END ##

## Lookup Orders START ##
def orders(oids = ""):
	endpoint = "/v3/orders/"
	try:
		endpoint += oids
		auth_header = getAuthorizationHeaderGET(endpoint)
		
		headers = {"Authorization":auth_header}
		response = getGETRequestHeaders(endpoint,headers)
	except requests.exceptions.RequestException as e:  
		print "Error: " + e
		return {}
	return response.content
## Lookup Orders END ##

## Cance Orders START ##
def cancel_orders(oids = ""):
	endpoint = "/v3/orders/"
	try:
		endpoint += oids
		auth_header = getAuthorizationHeaderDELETE(endpoint)
		
		headers = {"Authorization":auth_header}
		response = getDELETERequestHeaders(endpoint,headers)
	except requests.exceptions.RequestException as e:  
		print "Error: " + e
		return {}
	return response.content
## Cancel Orders END ##


## Place Orders START ##
def place_order(book, side, otype, major = "", minor="", price=""):
	endpoint = "/v3/orders/"
	try:
		
		payload_data = {"book":book, "side":side, "type":otype} 
		if major != "":
			payload_data["major"]=major
		else:
			payload_data["minor"]=minor

		if otype == "limit":
			payload_data["price"] = price

		json_payload = json.dumps(payload_data)
		auth_header = getAuthorizationHeaderPOST(endpoint, json_payload)
		
		headers = {"Authorization":auth_header,'content-type': "application/json"}
		response = getPOSTRequestPayload(endpoint, headers, json_payload)
	except requests.exceptions.RequestException as e:  
		print "Error: " + e
		return {}
	return response.content
## Place Orders END ##
