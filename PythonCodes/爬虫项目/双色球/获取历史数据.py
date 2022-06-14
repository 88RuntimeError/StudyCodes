# encoding='utf-8'
import requests
import time
import re


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'
}
with open('双色球各期网址数据.txt', 'r') as f:
    urls = eval(f.read())
keys = list(urls.keys())

with open('已经存储的id.txt', 'a+') as f:
    pass

with open('已经存储的id.txt', 'r') as f:
    history_id = f.read()
    if history_id:
        history_id = eval(history_id)
    else:
        history_id = []

with open('双色球各期历史数据.txt', 'a+') as f:
    pass

with open('双色球各期历史数据.txt', 'r') as f:
    dic = f.read()
    if dic:
        dic = eval(dic)
    else:
        dic = {}

for key in keys:
    id = key
    
    if id in history_id:
        continue
    else:
        url = urls[key]
        resp = requests.get(url, headers=headers)
        resp.encoding='gb2312'
        html = resp.text
        date = re.findall('开奖日期：(.*?) 兑奖截止日期', html)[0]
        red_ball = re.findall('<li class="ball_red">(\d+)</li>', html)
        blue_ball = re.findall('<li class="ball_blue">(\d+)</li>', html)[0]

        temp_dic = {}
        temp_dic['date'] = date
        temp_dic['red_ball'] = red_ball
        temp_dic['blue_ball'] = blue_ball
        dic[id] = temp_dic

        history_id.append(id)
        print(f'已更新数据{id}')
        resp.close()
        time.sleep(1)
    

with open('已经存储的id.txt', 'w') as f:
    f.write(str(history_id))

with open('双色球各期历史数据.txt', 'w') as f:
    f.write(str(dic))