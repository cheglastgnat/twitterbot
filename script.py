#!/usr/bin/env python
#-*- coding: utf-8 -*-


import random
import re
from subprocess import call, Popen, PIPE

## Yahoo! Weather RSS client (for WOEIDs)
import yweather

## Seed PRNG using current system time 
random.seed()


POSTS = [line.strip() for line in open('posts.txt').readlines()]
print POSTS

## The TTYtter executable
TTYTTER_BIN = "ttytter"

## Regular expression to extract hashtags from a list of trending topics
RE_TOPIC = re.compile(r'.*\"(?P<topic>#.*)\"')




## Get WOEID for Germany
yweather_client = yweather.Client()
WOEID_GER = yweather_client.fetch_woeid('Germany')

## Get trending topics for Germany
twitter_proc = Popen([TTYTTER_BIN, 
                      "-woeid=%d" % int(WOEID_GER),
                      "-runcommand=/trends"], 
                     stdout=PIPE)
## Extract #hashtags from trending topics
trending_topics = []
for line in iter(twitter_proc.stdout.readline, ''):
  m = RE_TOPIC.match(line)
  if m is not None:
    trending_topics.append(m.groupdict()['topic'])

## Randomly select a #hashtag ...
topic = trending_topics[random.randint(0,len(trending_topics)-1)]
## ... and a text to tweet
post = POSTS[random.randint(0,len(POSTS)-1)]

## Assemble tweet
tweet = "%s %s" % (post, topic)

## Post tweet to Twitter
call([TTYTTER_BIN, "-status=%s" % tweet])

