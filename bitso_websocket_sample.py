#!/usr/bin/python


import websocket

import socket
import thread
import time
import json
import datetime

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

def on_message(ws, message):
	data = json.loads(message)

	if 'action' in data and data['response'] == 'ok':
		print 'subscribed to %s channel at %s' % ( data['type'], datetime.datetime.fromtimestamp(data['time']/1000).strftime('%Y-%m-%d %H:%M:%S'))

	#{"type":"trades","book":"btc_mxn","payload":[{"i":4768575,"a":"0.0004824","r":"207300","v":"100.00152","mo":"svihYJLx72Fos9gV","to":"4iB3CldZWl6AMitZ","t":0}]}
	elif data['type']== 'trades':
		for entry in data['payload']:
			if entry['t'] == 0:
				print bcolors.OKGREEN + entry['r'] + bcolors.ENDC
			elif entry['t'] == 1:
				print bcolors.OKBLUE + entry['r'] + bcolors.ENDC
			else:
				print entry['r']
	elif data['type']  == 'diff-orders' and data['payload']:
		print data['payload']
	elif data['type']  == 'orders' and data['payload']:
		print data['payload']

def on_error(ws, error):
	print(error)

def on_close(ws):
	print("### closed ###")

def on_open(ws):
	ws.send(json.dumps({ "action": "subscribe", "book": "btc_mxn", "type": "trades" }));

	'''def run(*args):
		time.sleep(10000)
		ws.close()
		print "thread terminating..."

	thread.start_new_thread(run, ())'''

if __name__ == "__main__":
	websocket.enableTrace(True)
	#ws = websocket.WebSocketApp("wss://stream.binance.com:9443/ws/bnbbtc@depth",
	ws = websocket.WebSocketApp("wss://ws.bitso.com",
	on_message = on_message,
	on_error = on_error,
	on_close = on_close,
	on_open = on_open)
	ws.run_forever()


