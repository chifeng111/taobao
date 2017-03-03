__author__ = 'zhenhua'
#coding:utf-8
from openpyxl import Workbook
from get_html import get_page
from spider import parser

#设置想爬取的内容
content = '女裙'
filename = content + '.xlsx'


if __name__ == '__main__':
    wb = Workbook()
    ws = wb.active
    #获取100页源码列表
    html = get_page(content)
    #爬取商品名称，链接，价格
    ws.append(["商品名称", "链接地址", "价格"])
    for i in html:
        data = parser(i)
        for j in data:
            ws.append(j)
    wb.save(filename)
<<<<<<< HEAD
    print("爬取成功，已保存在%s文件中" %filename)
=======
    print("爬取成功，已保存在%s文件中" %filename)
>>>>>>> 61a2c5d2f40e5882d9cab508caeb9c0846d3108b
