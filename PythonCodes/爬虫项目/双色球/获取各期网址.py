import requests
from lxml import etree
from pymysql import *

html = requests.get('https://kaijiang.500.com/shtml/ssq/22052.shtml')
page = etree.HTML(html.text)

href_list = page.xpath('/html/body/div[6]/div[3]/div[2]/div[1]/div[1]/div[3]/span/div/a/@href')
page_id = page.xpath('/html/body/div[6]/div[3]/div[2]/div[1]/div[1]/div[3]/span/div/a/text()')
dic = {}

conn = connect(host='localhost',port=3306,user='root',password='123456',db='twocolorballs',charset='utf8')
cur = conn.cursor()

for index,i in enumerate(page_id):
    try:
        sql = "insert into urls values (%s,%s)"
        params = (i, href_list[index])
        cur.execute(sql,params)
        conn.commit()
        print(i,'增加成功!')
    except:
        conn.rollback()
        print('增加失败')
    
cur.close()
conn.close()






    
