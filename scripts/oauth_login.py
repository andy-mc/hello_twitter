#!/usr/bin/env python
# -*- coding: utf-8 -*-

import twitter

''' oauth_login into twitter '''

# Docs
# https://dev.twitter.com/oauth

# LogIn
def oauth_login():
	# credentials for OAuth
	CONSUMER_KEY = ' ---- '
	CONSUMER_SECRET = ' ---- '
	OAUTH_TOKEN = ' ---- ' 
	OAUTH_TOKEN_SECRET = ' ---- '
	
	# Creating the authentification
	auth = twitter.oauth.OAuth( OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET )
	
	# Twitter instance
	twitter_api = twitter.Twitter(auth=auth)
	return twitter_api

# LogIn
twitter_api = oauth_login()

print twitter_api
