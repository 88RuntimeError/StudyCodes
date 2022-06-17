#开发时间：2022/6/16 15:53
import requests
import re
import csv
import pandas as pd
headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://quote.eastmoney.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}
# 拼接URL，用于翻页爬虫
url_phase1 = 'http://www.cmbchina.com/cfweb/svrajax/product.ashx?op=search&type=m&pageindex='
url_phase2 = '&salestatus=&baoben=&currency=&term=&keyword=&series=01&risk=&city=&date=&pagesize=20&orderby=ord1&t=0.5589482005604671&citycode='
urls = []
Finacing = []

dict = {'PrdBrief': 1,'PrdCode': 1,'Risk': 1,'BeginDate': 1, 'EndDate': 1,
                     'ShowExpireDate': 1,'SaleChannelName': 1,'AreaCode': 1}
with open('000002.csv', 'w',newline='', encoding='utf_8_sig') as f:
        writer = csv.writer(f)
        writer.writerow(dict.keys())



for i in range(1, 11):
    urls.append(url_phase1 + str(i) + url_phase2)
# 通过for循环完成URL的遍历
for url in urls:
    # 获取源代码
    res = requests.get(url, headers=headers)
    res.encoding ='utf-8'
    page_content = res.text
    #理财产品名称
    PrdBrief = re.findall('PrdBrief:"(.*?)",', page_content)
    #代码
    PrdCode = re.findall('PrdCode:"(.*?)",', page_content)
    #风险评级
    Risk = re.findall('Risk:"(.*?)",', page_content)
    #发售起始日
    BeginDate = re.findall('BeginDate:"(.*?)",', page_content)
    #发售截止日
    EndDate = re.findall('EndDate:"(.*?)",', page_content)
    #产品到期日
    ShowExpireDate = re.findall('ShowExpireDate:"(.*?)",', page_content)
    #发售渠道
    SaleChannelName = re.findall('SaleChannelName:"(.*?)",', page_content)
    #发售行
    AreaCode = re.findall('AreaCode:"(.*?)",', page_content)
    # 数据存储到字典中
    dict = {'PrdBrief': PrdBrief,'PrdCode': PrdCode,'Risk': Risk,'BeginDate': BeginDate, 'EndDate': EndDate,
                     'ShowExpireDate': ShowExpireDate,'SaleChannelName': SaleChannelName,'AreaCode': AreaCode}
    with open('000002.csv', 'a',newline='', encoding='utf_8_sig') as f:
        writer = csv.writer(f)
        writer.writerows(zip(*dict.values()))
