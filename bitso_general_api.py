import time
import hmac
import hashlib
import requests
import json
import bitso_api_credentials

bitso_key = bitso_api_credentials.bitso_key
bitso_secret = bitso_api_credentials.bitso_secret
baseUri = bitso_api_credentials.baseUri

def getQueryParameters(params):
	query = "?"
	for majorkey, value in params.iteritems():
		
		if (value != ""):
			if query != "?":
				query += "&"
			query += majorkey+"="+value

	return query

def getRequest (method, url, headers, params, data = "" ):
	return requests.request(method, url, headers=headers, params=params, data = data)

def getGETRequestParams(endpoint, params=""):
	return getRequest("GET", baseUri+endpoint,"",params)

def getGETRequestHeaders(endpoint, headers):
	return getRequest("GET", baseUri+endpoint,headers, "")

def getGETRequest(endpoint, headers="", params=""):
	return getRequest("GET", baseUri+endpoint,headers, params)

def getPOSTRequest(endpoint, params=""):
	return getRequest("POST", baseUri+endpoint,"",params)

def getPOSTRequestHeaders(endpoint, headers):
	return getRequest("POST", baseUri+endpoint,headers,"")

def getPOSTRequestPayload(endpoint, headers,json_payload):
	return getRequest("POST", baseUri+endpoint,headers,"",json_payload)

def getDELETERequestHeaders(endpoint, headers):
	return getRequest("DELETE", baseUri+endpoint,headers, "")

def getNonce():
	return str(int(round(time.time() * 1000)))

def getMessage(nonce, http_method,request_path, json_payload=""):
	return nonce+http_method+request_path+json_payload

def getSignature(secret, message):
	return hmac.new(secret.encode('utf-8'),
                                            message.encode('utf-8'),
                                            hashlib.sha256).hexdigest()
def getAuthHeader(key, nonce, signature):
	return 'Bitso %s:%s:%s' % (key, nonce, signature)


