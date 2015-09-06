import urllib2
import json

def getTweets(url):
	mtaData = json.load(url)
	fixedData = json.loads(mtaData)
	print(fixedData.keys())