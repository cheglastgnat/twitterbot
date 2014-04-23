#!/usr/bin/env python3
#-*- coding: utf-8 -*-

##
#
# 
#
##

## Imports
import random
import re
from subprocess import call, Popen, PIPE
## Local imports
from core import get_trending_topics_for_country, tweet, TTYTTER_BIN

## Seed PRNG using current system time
random.seed()


def post_random_content_with_trending_hashtag():
    """
        Post a random comment to Twitter, together with a random
        trending hashtagged topic.
    """

    ## Read a list of available tweet texts.
    POSTS = [line.strip() for line in open('posts.txt').readlines()]

    ## Get trending topics for Germany
    trending_topics = get_trending_topics_for_country("Germany")

    ## Randomly select a #hashtag ...
    topic = trending_topics[random.randint(0,len(trending_topics)-1)]
    ## ... and a text to tweet
    post = POSTS[random.randint(0,len(POSTS)-1)]

    ## Assemble tweet ...
    content = "%s %s" % (post, topic)
    ## ... and post it
    tweet(content)


##
# MAIN CALL
##
if __name__ == "__main__":
    post_random_content_with_trending_hashtag()
