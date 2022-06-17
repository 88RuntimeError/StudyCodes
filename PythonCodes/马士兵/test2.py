# yyx's first attempt
# 开发时间: 2022/6/16 19:51
# yyx's first attempt
# 开发时间: 2022/6/16 00:05
import json

import requests
import bs4
from urllib import parse
url = "https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page=0&iOrder=0&iSortNumClose=1&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1655308252639"
headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"}
def send_resquest():#发送请求
    resp = requests.get(url,headers=headers)
    return resp.text
def exact_list(data):#批量提取数据中的网址
    image_url_lst=[]
    for i in range(1,9):
        print('data = ',data)
        
        data_lst=parse.unquote(data["sProdName_1"]).replace('200','0')
        break
        image_url_lst.append(data_lst)
    print(image_url_lst)
def parse_html(data):  # 解析url
    s = data.replace('jQuery171013558800688010786_1655307952986(', '').replace(');', '')
    data1=json.loads(s)
    data2=data1["List"]
    data_lst={}
    for data in data2:
        image_url_lst=exact_list(data)
        data['sProdName']=parse.quote(data['sProdName'])
        data_lst["sProdName"]=image_url_lst
        for item in data_lst:
            print(item,data_lst[item])
def start():
    data = send_resquest()
    parse_html(data)
if __name__ == '__main__':
    start()