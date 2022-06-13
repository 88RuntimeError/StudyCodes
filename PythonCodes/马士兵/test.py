#导入模块
import requests
import re
# #定义请求url
url = "https://wkbjcloudbos.bdimg.com/v1/docconvert2386/wk/624e0eea16ebd6547fba416eb3853766/0.json?responseContentType=application%2Fjavascript&responseCacheControl=max-age%3D3888000&responseExpires=Wed%2C%2028%20Apr%202021%2022%3A28%3A19%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2021-03-14T14%3A28%3A19Z%2F3600%2Fhost%2Fb2a4cf6ad592d3ba2b13baa3d08432bf5835e25a5bd0b412e065cf8eed4d3f86&x-bce-range=0-68281&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTYxNTczNTY5OSwidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.OBktypfIcH7bHU3FrUik7n%2FThMKUksNx58yYL5orhS0%3D.1615735699"
#定义请求头
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50"}
# #请求内容
response = requests.get(url=url,headers=headers)
#print(response)
# #设置编码方式
response.encoding = 'unicode_escape'
list = []
# #正则提取所需要的内容
response_list = re.findall(r'"c":(.*?),"',response.text)
# #循环打印
for sentence in response_list:
    if sentence[0] == '"':
        #re.findall(r'"(.*?)"',sentence)
        sentence = sentence[1:]
        sentence = sentence[:-1]
        print(sentence,end='') 