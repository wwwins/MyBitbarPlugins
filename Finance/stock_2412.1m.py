#!/usr/bin/env python
# -*- coding: utf-8 -*-
# <bitbar.title>Stock Price</bitbar.title>
# <bitbar.version>1.0</bitbar.version>
# <bitbar.author>wwwins</bitbar.author>
# <bitbar.author.github>wwwins</bitbar.author.github>
# <bitbar.desc>Display Stock Price</bitbar.desc>
# <bitbar.image></bitbar.image>

import requests
import time
from lxml import html

# Setting price to buy a stock
BUY_PRICE = 95.0
STOCK = "2412"
color = "steelblue"

HEADER = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A366 Safari/600.1.4'}
URL = 'https://tw.stock.yahoo.com/q/q?s='+STOCK+'&_ts='

if (int(time.strftime("%H")) > 17):
	print ('🈚️')
	exit()

if (int(time.strftime("%H")) < 9):
	print ('🈚️')
	exit()

ts = str(int(time.time()));
r = requests.get(URL+ts, headers=HEADER)
doc = html.fromstring(r.content)
content = doc.cssselect("b")
if not content:
	print ('🈚️')
	exit()
price = content[0].text
if (float(price) < BUY_PRICE):
	color = "red"
print ('Chunghwa:'+price+'| color='+color)
