__author__ = 'zhenhua'
from bs4 import BeautifulSoup


def parser(html):
    soup = BeautifulSoup(html, 'html.parser', from_encoding='gbk')
    item = soup.find_all('li', class_=' item item-border')
    data = []
    for i in item:
        a = i.find('div', class_='title child-component').find('a')
        title = a.get_text()
        link = a['href']
        b = i.find('div', class_='price child-component clearfix').find('strong')
        price = b.get_text()
        #print("%s \t %s \t %s" %(title, link, price))
        data.append([title, link, price])
    return data