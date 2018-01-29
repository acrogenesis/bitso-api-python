#!/usr/bin/python

from bitso_general_api import *

#BITSO PUBLIC API

## Available books START ##
def available_books():
	endpoint = "/v3/available_books/"
	try:
		response = getGETRequest(endpoint)
	except requests.exceptions.RequestException as e:  
		print "Error: " + e
		return {}

	return response.content
## Available books END ##

## Price Ticker START ##
def price_ticker(book):
	endpoint = "/v3/ticker/"
	try:
		response = getGETRequestParams(endpoint, {"book":book})
	except requests.exceptions.RequestException as e:  
		print "Error: " + e
		return {}

	return response.content
## Available books END ##

## order book START ##
def order_book(book, aggregate="false"):
	endpoint = "/v3/order_book/"
	try:
		response = getGETRequestParams(endpoint, {"book":book,"aggregate":aggregate})
	except requests.exceptions.RequestException as e:  
		print "Error: " + e
		return {}

	return response.content
## order book END ##

## order book START ##
def trades(book, marker="", sort="desc", limit="25"):
	endpoint = "/v3/trades/"
	try:
		response = getGETRequestParams(endpoint, {"book":book,"marker":marker, "sort":sort, "limit":limit})
	except requests.exceptions.RequestException as e:  
		print "Error: " + e
		return {}

	return response.content
## order book END ##
