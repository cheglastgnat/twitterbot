#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
	A command line interface for the twitterbot functions
	both for testing and showing off purposes
"""
import sys

from core import get_trending_topics_for_country, get_followers

def show_trending_hashtags(country):
	"""
		Tries to get the trending hashtags for the given
		country and displays them
	"""
	trends = get_trending_topics_for_country(country)

	print trends

def show_followers(user=None):
	followers = get_followers(user)

	print followers

if __name__ == "__main__":

	available_commands = {
		"trending": show_trending_hashtags,
		"followers": show_followers
	}

	selected_command = sys.argv[1]

	try:
		# run the selected command with the rest of the arguments
		available_commands[selected_command](*sys.argv[2:])
	except KeyError:
		print "Unknown command. Available commands are:"
		print "{0}".format(available_commands.keys())
