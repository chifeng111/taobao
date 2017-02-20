__author__ = 'zhenhua'
#coding:utf-8
from get_html import get_page
from spider import parser

if __name__ == '__main__':
    #获取100页源码列表
    html = get_page("裙子")
    for i in html:
        parser(i)
        print('-'*150)