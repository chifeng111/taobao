# taobao
###基于selenium和BeautifulSoup的淘宝网商品信息爬取。

======
####项目中主要包括3个文件，其中main.py是项目入口，负责将获取的信息写入excel。get_html.py主要获取淘宝搜索页源码，每个搜索有100页，获取100页源码返回。spider.py主要分析源码，从源码中得到需要的信息。

----
####程序主入口main.py
![image](https://github.com/chifeng111/taobao/raw/master/img/1.jpg)

####共爬取6000多条商品信息
![image](https://github.com/chifeng111/taobao/raw/master/img/2.jpg)
