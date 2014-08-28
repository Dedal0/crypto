#!/usr/bin/python

#btccheck.py (c)
#btccheck.py is a script to get the balance of any btc account.

import urllib
import json

btcdir = raw_input("Input the BTC Account")

url = 'https://api.chain.com/v1/bitcoin/addresses/' + btcdir + '?key=DEMO-4a5e1e4'
html = urllib.urlopen(url).read().decode('utf-8')
j = json.loads(html)
balance = j['balance'] / 100000000.0

print balance
