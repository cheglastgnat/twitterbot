#!/usr/bin/env python3
#-*- coding: utf-8 -*-

##
#
# Helper module for obtaining short page gists from Wikipedia.
#
# © Nikolaus Mayer, 2014
#
# REQUIRED SOFTWARE:
# ==================
# Python's "requests" module. Find it at
#   python-requests.org
# Install using pip
# > pip install requests
# or easy_install
# > easy_install requests
# or find it on GitHub:
#   https://github.com/kennethreitz/requests
#
##

## Imports
## 'Requests' module for GETting stuff from the web
import requests

## JSON for parsing
import json
import re


class WikiSnippet:
    def __init__(self, language_code='en'):
        """
            Constructor
            @param language_code The language_code for the target Wikipedia
              site, see <http://meta.wikimedia.org/wiki/Special:SiteMatrix>
        """
        ## Regular expressions for tidying up the raw response text
        ## Delete XML tags
        self.RE_XML_TAG = re.compile(r'<\/?[^>]+>')
        ## Convert newlines to spaces
        self.RE_NEWLINES_AND_SPACE = re.compile(r'(?:\\n)+')

        self.parameters = {}
        self.parameters['language_code'] = language_code
        self.request_template = 'http://{language_code}.wikipedia.org/w'\
                                '/api.php?action=query'                 \
                                '&prop=extracts'                        \
                                '&format=json'                          \
                                '&exchars={max_length}'                 \
                                '&exlimit=1'                            \
                                '&titles={topic}'

    def GetSnippet(self, topic='', max_length=100):
        """
            Try to query Wikipedia
            @param topic The desired page name from which the snippet
                         should be read
            @param max_length The maximum length of the snippet
            @returns the first max_length characters (TODO: more or less)
                     of the Wikipedia page for the specified topic
        """
        self.parameters['topic'] = topic
        ## For safety, retrieve a longer response (the result is likely
        #  to contain useless XML tags etc.
        self.parameters['max_length'] = max_length*3
        ## Retrieve raw JSON data from Wikipedia
        try:
            req = requests.get(self.request_template.format(**self.parameters))
        except:
            print(' ERROR: Could not get a response from Wikipedia!')
            return ''

        ## Parse JSON structure
        try:
            as_json = json.loads(req.text)
        except:
            print(' ERROR: Could not parse response JSON structure!')
            return ''
        ## Get the actual page text from the JSON response (the convoluted
        #  structure is just what the response happens to look like)
        try:
            text = json.dumps(as_json['query']['pages'].popitem()[1]['extract'])
        except:
            print(' ERROR: Invalid response structure (does the desired'
                  ' page exist?)')
            return ''
        ## Clean up the text (delete XML tags and newlines)
        text = re.sub(self.RE_XML_TAG, '', text)
        text = re.sub(self.RE_NEWLINES_AND_SPACE, ' ', text)
        ## Clip result length
        if len(text) > self.parameters['max_length']//3:
            clip_index = self.parameters['max_length']//3
            ## Don't cut off in the middle of a word
            while text[clip_index] != ' ':
                clip_index -= 1
            text = text[:clip_index]+'...'

        ## Return the result
        return text



## If this module is called as a standalone, do a test run
if __name__=='__main__':
    print('This is what en.wikipedia.org has to say about Isaac Asimov...')
    print('')
    test_instance = WikiSnippet('en')
    text = bytes(test_instance.GetSnippet('Isaac Asimov', 200), "ascii")
    print(text.decode("unicode_escape"))
    print('')


