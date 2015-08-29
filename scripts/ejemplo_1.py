#!\usr\bin\env python
# -*- coding:utf-8 -*-

# https://dev.twitter.com/rest/reference/get/search/tweets

import twitter
import json

def oauth_login():
	# credentials for OAuth
	CONSUMER_KEY = ' ---- '
	CONSUMER_SECRET =' ---- '
	OAUTH_TOKEN = ' ---- '
	OAUTH_TOKEN_SECRET = ' ---- '
	
	# Creating the authentification
	auth = twitter.oauth.OAuth( OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET )
	
	# Twitter instance
	twitter_api = twitter.Twitter(auth=auth)
	return twitter_api

# LogIn
twitter_api = oauth_login()

# Search tweets with the query (q) 
results = twitter_api.search.tweets(q='chapo', count=1)
print json.dumps(results, indent=5)
