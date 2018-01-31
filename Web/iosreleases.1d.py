#!/usr/bin/env python
# -*- coding: utf-8 -*-
# <bitbar.title>Get tweets for the latest iOS releases</bitbar.title>
# <bitbar.version>1.0</bitbar.version>
# <bitbar.author>wwwins</bitbar.author>
# <bitbar.author.github>wwwins</bitbar.author.github>
# <bitbar.desc>Get tweets for the latest iOS releases</bitbar.desc>
# <bitbar.image></bitbar.image>

import datetime

from urllib2 import urlopen
from urllib2 import Request
from lxml import etree

#RSS_URL = "http://twitrss.me/twitter_user_to_rss/?user=iOSReleases"
RSS_URL = "http://ipsw.me/timeline.rss"
color = "slateblue"
ios_version = ""

def format_text(dic):
    return (u'%s | href=https://twitter.com/iOSReleases' % dic['desc'].replace('9.9.','')).encode('utf-8')

req = Request(RSS_URL, headers={'User-Agent':'Mozilla/5.0'})
doc = etree.parse(urlopen(req))
root = doc.getroot()

unique_set = set()
unique_arr = []

for child in root[0][6:]:
    title = child[0].text
    if 'iOS' in title:
        if title not in unique_set:
            unique_set.add(title)
            unique_arr.append({'title':title, 'desc':child[2].text, 'date':child[3].text})

result = sorted(unique_arr, key=lambda x:datetime.datetime.strptime(x['date'], '%a, %d %b %Y %X +%f'), reverse=True)

for item in result[0:10]:
    if ios_version=="":
        s = item['title'].split(' ')
        ios_version = s[2]
        if len(s) > 3:
            ios_version = s[2]
        print(u'iOS:'+ios_version+"|color="+color).encode('utf-8')
        print('---')
    print format_text(item)
print('---')
