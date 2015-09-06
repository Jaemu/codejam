import urllib2
import json
from bs4 import BeautifulSoup as bs

def getTweets():
	#mtaData = json.load(urllib2.urlopen('https://twitter.com/i/profiles/show/LIRR/timeline.json'))
	#strData = json.dumps(mtaData)
	#mtaData = json.loads(strData)
	#htmlDoc = mtaData[u'items_html']
	newHtml = open('mta.html', 'r')
	soup = bs(newHtml, 'html.parser')
	betterData = soup.get_text().replace('\n', '').split('NOT monitored')[1].split('LIRR')
	pData = soup.find_all('p', 'tweet-text')
	trains = {}
	for tweet in xrange(len(pData)):
		print(pData[tweet].contents)


if __name__ == '__main__':
	getTweets()