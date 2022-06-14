import requests
import os
from lxml import etree

html = requests.get('https://kaijiang.500.com/shtml/ssq/22052.shtml')
page = etree.HTML(html.text)

href_list = page.xpath('/html/body/div[6]/div[3]/div[2]/div[1]/div[1]/div[3]/span/div/a/@href')
page_id = page.xpath('/html/body/div[6]/div[3]/div[2]/div[1]/div[1]/div[3]/span/div/a/text()')
dic = {}
for index,i in enumerate(page_id):
    dic[i] = href_list[index]   

if not os.path.exists('双色球各期网址数据.txt'):
    with open('双色球各期网址数据.txt', 'w') as f:
        pass

with open('双色球各期网址数据.txt', 'r') as f:
    resource = f.read()
    if resource:
        resource = eval(resource)


if not resource:
    with open('双色球各期网址数据.txt', 'w') as file:
        file.write(str(dic))
        print('已新建双色球各期网址数据')

else:
    dic.update(resource)
    with open('双色球各期网址数据.txt', 'w') as file:
        file.write(str(dic))
        print('已更新双色球各期网址数据')
    
