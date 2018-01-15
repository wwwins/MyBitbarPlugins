#!/usr/bin/env python
# -*- coding: utf-8 -*-
# <bitbar.title>Get tweets for the latest iOS releases</bitbar.title>
# <bitbar.version>1.0</bitbar.version>
# <bitbar.author>wwwins</bitbar.author>
# <bitbar.author.github>wwwins</bitbar.author.github>
# <bitbar.desc>Get tweets for the latest iOS releases</bitbar.desc>
# <bitbar.image></bitbar.image>

from lxml import etree

color = "slateblue"
ios_version = ""

def format_text(xml):
	return (u'%s | href=%s' % (xml[0].text, xml[5].text)).encode('utf-8')

doc = etree.parse("http://twitrss.me/twitter_user_to_rss/?user=iOSReleases")
root = doc.getroot()

for child in root[0][6:]:
	if "iOS" in child[0].text:
		start = child[0].text.index('for ')
		end = child[0].text.index(' device')
		cnt_devices = int(child[0].text[start+4:end])
		if cnt_devices>10:
			if ios_version=="":
				ios_version = child[0].text.split(' ')[1]
				print(u'iOS:'+ios_version+"|color="+color).encode('utf-8')
				print('---')
			print format_text(child)
print('---')
