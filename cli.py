#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
    A command line interface for the twitterbot functions
    both for testing and showing off purposes
"""

## Imports
import sys
## Local imports
from core import get_trending_topics_for_country, get_followers


def show_trending_hashtags(location_name):
    """
        Tries to get the trending hashtags for the given
        location and prints them.
        
        @param location_name Name of the target location (see core.py)
    """
    trends = get_trending_topics_for_country(location_name)
    print(trends)


def show_followers(user=None):
    followers = get_followers(user)

    print(followers)


##
# MAIN CALL
##
if __name__ == "__main__":

    ## List of valid command strings
    available_commands = {
        "trending": show_trending_hashtags,
        "followers": show_followers
    }
    pretty_commands = ", ".join([c for c in available_commands.keys()])

    ## Sanity check/ help
    if len(sys.argv) < 2:
        print("Usage: {0} <command> [arguments]".format(sys.argv[0]))
        print("Available commands are: {0}".format(pretty_commands))
        quit()

    selected_command = sys.argv[1]

    try:
        ## Run the selected command with the rest of the arguments
        available_commands[selected_command](*sys.argv[2:])
    except KeyError:
        print("Unknown command '{0}'!".format(sys.argv[1]))
        print("Available commands are: {0}".format(pretty_commands))

