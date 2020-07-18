import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')

# print(soup.find_all('a'))
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def custom_hacker_news(links, subtext):
    hm = []
    for id, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None) # If link is broken replace it with None
        vote = subtext[id].select('.score')
        if len(vote):
            points = int(vote[0].getText().split(' ')[0])
            if points >= 100:
                hm.append({'title': title,'link': href, 'point': points})
    return hm

pprint.pprint(custom_hacker_news(links, subtext))