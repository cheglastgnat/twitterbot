#!/usr/bin/env python
#-*- coding: utf-8 -*-


import random
import re
from subprocess import call, Popen, PIPE

from core import get_trending_topics_for_country, tweet


def post_random_content_with_trending_hashtag():
	## Seed PRNG using current system time
	random.seed()

	POSTS = [line.strip() for line in open('posts.txt').readlines()]

	## The TTYtter executable
	TTYTTER_BIN = "./TTYitter.pl"

	trending_topics = get_trending_topics_for_country("Germany")

	## Randomly select a #hashtag ...
	topic = trending_topics[random.randint(0,len(trending_topics)-1)]
	## ... and a text to tweet
	post = POSTS[random.randint(0,len(POSTS)-1)]

	## Assemble tweet
	content = "%s %s" % (post, topic)

	tweet(content)

if __name__ == "__main__":
	post_random_content_with_trending_hashtag()
