__author__ = 'zhenhua'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def get_page(key_words):
    html = []
    b = webdriver.PhantomJS(executable_path="phantomjs.exe")
    #b = webdriver.Firefox()
    b.get("https://world.taobao.com/")
    time.sleep(3)
    b.find_element_by_id('q').send_keys(key_words)
    b.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]/div[2]/form/div[1]/button').click()
    time.sleep(3)
    b.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    b.maximize_window()
    html.append(b.page_source.encode('gbk', 'ignore'))
    for i in range(99):
        b.find_element_by_xpath('/html/body/div[5]/div[4]/div/div[1]/div[1]/div[4]/div/div/a[last()]/span').click()
        page = str(i+1)
        time.sleep(5)
        b.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        html.append(b.page_source.encode('gbk', 'ignore'))
        print("正在爬取第%s页" %page)
    b.close()
    return html

#/html/body/div[5]/div[4]/div/div[1]/div[1]/div[4]/div/div/a[last()]/span
#/html/body/div[5]/div[4]/div/div[1]/div[1]/div[4]/div/div/a[7]/span
