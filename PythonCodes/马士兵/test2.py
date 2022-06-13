import requests
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'
}
resp = requests.get('https://search.jd.com/Search?keyword=%E9%9E%8B%E5%AD%90&psort=4&wq=%E9%9E%8B%E5%AD%90&psort=4&pvid=d5fcd082688f4a7e805ba4f5b56ae20d&click=1',headers=headers)

print(resp.text)