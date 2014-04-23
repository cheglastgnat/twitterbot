#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re

## Yahoo! Weather RSS client (for WOEIDs)
import yweather
from subprocess import call, Popen, PIPE

TTYTTER_BIN = "./TTYitter.pl"

## Regular expression to extract hashtags from a list of trending topics
RE_TOPIC = re.compile(r'.*\"(?P<topic>#.*)\"')

## Regular expression to extract twitter handles from followers
RE_FOLLOWERS = re.compile(r'\S[^\(\)]+\(([^\(\)]+)\).*')

def get_trending_topics_for_country(country):
    """
        Returns a list of the trending hashtags for a given country
    """
    ## Get WOEID for Germany
    yweather_client = yweather.Client()
    WOEID = yweather_client.fetch_woeid(country)

    ## Get trending topics for the country
    twitter_proc = Popen([TTYTTER_BIN,
                          "-woeid=%d" % int(WOEID),
                          "-runcommand=/trends"],
                         stdout=PIPE)

    ## Extract #hashtags from trending topics
    trending_topics = []
    for line in iter(twitter_proc.stdout.readline, ''):
        m = RE_TOPIC.match(line)
        if m is not None:
            trending_topics.append(m.groupdict()['topic'])

    return trending_topics

def get_followers(user=None):
    """
        returns a list of twitter handles of all followers of the
        given user. If user is none returns own followers
    """
    if user is None:
        proc = Popen(
            [TTYTTER_BIN, "-runcommand=/followers"],
            stdout=PIPE
        )
    else:
        proc = Popen(
            [TTYTTER_BIN, "-runcommand=/followers %s" % user],
            stdout=PIPE
        )

    followers = []

    for line in iter(proc.stdout.readline, ''):
        m = RE_FOLLOWERS.match(line)
        if m:
            followers.append(m.group(1))

    return followers

def tweet(tweet_content):
    ## Post tweet to Twitter
    call([TTYTTER_BIN, "-status=%s" % tweet_content])
