import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')

# print(soup.find_all('a'))
links = soup.select('.storylink')
votes = soup.select('.score')

def custom_hacker_news(links, votes):
    hm = []
    for id, item in enumerate(links):
        title = links[id].getText()
        href = links[id].get('href', None) # If link is broken replace it with None
        points = int(votes[id].getText().split(' ')[0])
        if points >= 100:
            hm.append({'title': title,'link': href, 'point': points})
    return hm

print(custom_hacker_news(links, votes))