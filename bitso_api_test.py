#!/usr/bin/python

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

from bitso_public_api import *
from bitso_private_api import *


print bcolors.HEADER +  "## bitso public api ##\n\n"  + bcolors.ENDC

print bcolors.BOLD + "Available books: \n" + bcolors.ENDC + available_books()

print bcolors.BOLD + "\n\nPrice for ETH/BTC: \n" + bcolors.ENDC + price_ticker("eth_btc")
print bcolors.BOLD + "\nOrder bok for ETH/BTC: \n" + bcolors.ENDC + order_book("eth_btc", "true")
print bcolors.BOLD + "\nTrades for ETH/BTC: \n" + bcolors.ENDC + trades("eth_btc")


print bcolors.HEADER +  "\n\n## bitso private api ##\n\n"  + bcolors.ENDC
print bcolors.BOLD + "\nAccount Status: \n" + bcolors.ENDC + account_status()

print bcolors.BOLD + "\nAccount Balance: \n" + bcolors.ENDC + account_balance()
print bcolors.BOLD + "\nfees: \n" + bcolors.ENDC + fees()

print bcolors.BOLD + "\nledger: \n" + bcolors.ENDC + ledger("17c4780adf0450f70edcbf9eee156098","desc","2")
print bcolors.BOLD + "\nledger trades: \n" + bcolors.ENDC + ledger("","desc","2", "trades/")
print bcolors.BOLD + "\nledger fees: \n" + bcolors.ENDC + ledger("","desc","2", "fees/")
print bcolors.BOLD + "\nledger funding: \n" + bcolors.ENDC + ledger("","desc","2", "fundings/")
print bcolors.BOLD + "\nledger withdrawals: \n" + bcolors.ENDC + ledger("","desc","2", "withdrawals/")

print bcolors.BOLD + "\nuser trades: \n" + bcolors.ENDC + user_trades("","desc","4", "")
print bcolors.BOLD + "\nuser trades tid: \n" + bcolors.ENDC + user_trades("","desc","", "/4736228")
print bcolors.BOLD + "\nuser trades tid-tid: \n" + bcolors.ENDC + user_trades("","desc","", "/4736228-4731126")

print bcolors.BOLD + "\norder trades: \n" + bcolors.ENDC +order_trades("HffYZ3k3Ff8ESgMM")
print bcolors.BOLD + "\norder trades: \n" + bcolors.ENDC +order_trades("ov4RUy1hPlLO2WC")

print bcolors.BOLD + "\nopen orders: \n" + bcolors.ENDC + open_orders("eth_btc")

print bcolors.BOLD + "\norders: \n" + bcolors.ENDC + orders("HffYZ3k3Ff8ESgMM")
print bcolors.BOLD + "\norders: \n" + bcolors.ENDC + orders("HffYZ3k3Ff8ESgMM-ov4RUy1hPlLO2WC")

#print bcolors.BOLD + "\n cancel orders: \n" + bcolors.ENDC + cancel_orders("C4CqAlX0mY5ogLVH")

#print bcolors.BOLD + "\n place orders: \n" + bcolors.ENDC + place_order("eth_btc", "sell", "limit", "0.001", "", "1.0000")
