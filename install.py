#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#!
#
# Installation and setup script
#
##

#imports
import urllib.request
import stat
import os
import configparser
import sys

##################
# default values #
##################
TTYtterUrl='http://www.floodgap.com/software/ttytter/dist2/2.1.00.txt'
TTYtterFilePath='./'

TrendingTopicsCountry='Germany'

##################
# Install prompt #
##################
print("In order to install twitterbot, please setup some variables.")
TTYtterUrl=input("Url to the newest TTYtter file ["+TTYtterUrl+"]") or TTYtterUrl
TTYtterFilePath=input("Install dir of TTYtter ["+TTYtterFilePath+"]") or TTYtterFilePath
TrendingTopicsCountry=input("Country of trending topics that will be randomly" 
                            "selected ["+TrendingTopicsCountry+"]") or TrendingTopicsCountry


print("--------------------------------------")
##############################
# Setup TTYtter command file #
##############################
print("Downloading and setting up TTYtter!")
print("This may take some while...")
# download TTYtter
response = urllib.request.urlopen(TTYtterUrl)
# get online ressource and decode as string
TTYtterFileContent = response.read().decode('utf-8')

# write file
TTYtterFileLocation=TTYtterFilePath+'/TTYtter'
TTYtterFile = open(TTYtterFileLocation, 'w')
TTYtterFile.write(TTYtterFileContent)
TTYtterFile.close()

# make file executable
st = os.stat(TTYtterFileLocation)
os.chmod(TTYtterFileLocation, st.st_mode | stat.S_IEXEC)


#######################
# writing config file #
#######################
print("Writing config file...")
config = configparser.ConfigParser()

config['core'] = {'TTYtterBin': TTYtterFileLocation}
config['script'] = {'TrendingTopicsCountry': TrendingTopicsCountry}

with open('config/twitterbot.cfg', 'w') as configfile:
  config.write(configfile)

print("--------------------------------------")
print("Installation completed!")