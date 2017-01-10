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

if (int(time.strftime("%H")) > 17):
	print ('🈚️')
	exit()

if (int(time.strftime("%H")) < 9):
	print ('🈚️')
	exit()

ts = int(time.time());
r = requests.get("https://tw.m.yahoo.com/w/twstock/index_single.php?_ts="+str(ts)+"&_httpHost=tw.m.yahoo.com&_intl=tw&_lang=zh-hant-tw&stock="+STOCK)
doc = html.fromstring(r.content)
content = doc.cssselect("tr.odd")
if not content:
	print ('🈚️')
	exit()
price = content[0][2].text
if (float(price) < BUY_PRICE):
	color = "red"
print ('Chunghwa:'+price+'| color='+color)
