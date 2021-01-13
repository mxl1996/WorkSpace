# 需求
import requests

if __name__ == '__main__':
    url = 'https://www.baidu.com/s?wd=ip'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    # 添加代理IP
    response = requests.get(url=url, headers=headers,proxies={"https":'14.207.29.238:8080'}).text
    with open('ip.html', 'w',encoding='utf-8') as fp:
        fp.write(response)