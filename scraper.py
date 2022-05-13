import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.bbc.com/zhongwen/trad/topics/c83plve5vmjt')

soup = BeautifulSoup(response.text, 'lxml')
titles = soup.find_all('span', {'class': 'lx-stream-post__header-text gs-u-align-middle'})

title_list = []
for title in titles:
    title_list.append(title.getText())

urls = soup.find_all('a', {'class': 'qa-heading-link lx-stream-post__header-link'})

tag_list = []
for url in urls:
    sub_response = requests.get('https://www.bbc.com' + url.get('href'))
    sub_soup = BeautifulSoup(sub_response.text, 'lxml')
    tags = sub_soup.find_all('li', {'class': 'bbc-1msyfg1 e1hq59l0'})
    for tag in tags:
        tag_list.append(tag.getText())
        
print(tag_list)