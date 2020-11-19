import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text,'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def sort_stories_by_vote(newlist):
	return sorted(newlist, key = lambda k : k['votes'], reverse = True )

def create_custom_hn(links, subtext):
	h_news = []
	for idx,item in enumerate(links):
		title = links[idx].getText()
		href = links[idx].get('href',None)
		vote = subtext[idx].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace(' points', ''))
			if points> 99:
				h_news.append({'title': title, 'hlink': href, 'votes': points})
	return sort_stories_by_vote(h_news)

pprint.pprint(create_custom_hn(links,subtext))