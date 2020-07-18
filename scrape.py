import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')

# print(soup.find_all('a'))
links = soup.select('.storylink')
votes = soup.select('.score')