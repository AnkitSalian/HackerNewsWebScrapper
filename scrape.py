import requests
from bs4 import BeautifulSoup
import pprint
import sys

def get_hacker_news(page_no):
    res = requests.get('https://news.ycombinator.com/news?p=1')
    soup = BeautifulSoup(res.text, 'html.parser')

    # print(soup.find_all('a'))
    links = soup.select('.storylink')
    subtext = soup.select('.subtext')
    return custom_hacker_news(links, subtext)

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['point'], reverse=True)

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


try:
    # No of pages scrapping to be done
    total_pages = int(sys.argv[1])
    mega_news = []
    for i in range(total_pages):
        mega_news += get_hacker_news(i+1)
    sorted_mega_news = sort_stories_by_votes(mega_news)
    pprint.pprint(sorted_mega_news)
    print(len(sorted_mega_news))
except ValueError:
    print('Pass a valid number greater than zero')