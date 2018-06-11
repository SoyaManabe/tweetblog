#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
import sys
print(sys.version_info)
"""

import twitter
import random


auth = twitter.OAuth(consumer_key="i04bQrT9ZMBMcmR5Jr3KCM7DM",
consumer_secret="xgAox7qp3xROcJVcIiRjzhxSneIoQDNzxyF0ttUVGjfnCRBJFS",
token="862481526016978948-GmiGQnknmym07IYmppjJIQbaEO1zh1j",
token_secret="uXFuB6tj3bBWVgPUNSr2d5SeIA6QTwpRuTvEL7KpcqrrW")

t = twitter.Twitter(auth=auth)

list = ["バイトやあ", "眠い", "こんにちは","おやすみ"]

i  = random.randint(0,len(list))

#ツイートのみ
status=list[i] #投稿するツイート
t.statuses.update(status=status) #Twitterに投稿
