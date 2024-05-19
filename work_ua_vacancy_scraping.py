import requests
from bs4 import BeautifulSoup

start_page = int(input())
last_page = int(input())


#Returns list with pagination links
def get_pagination_page_links(url):
    links = []

    for i in range(start_page, last_page + 1):
        links.append(url + str(i))
    return links


#Displays a list of titles and links on one page
def get_title_and_link(page_link):
    req = requests.get(page_link)
    soup = BeautifulSoup(req.content, 'lxml')
    key_words = soup.find_all('h2', class_='cut-bottom')

    for word in key_words:
        link = word.a
        if link:
            print(link['title'], " ", 'https://www.work.ua', link['href'], sep='')
            # return link['title'] + ' ' + 'https://www.work.ua' + link['href']


link_prod = get_pagination_page_links('https://www.work.ua/jobs/?page=')


#Lists titles and links on all requested pages
def get_links_and_titles(lin):
    for link in lin:
        print('Page', link[-1])
        get_title_and_link(link)


get_links_and_titles(link_prod)
