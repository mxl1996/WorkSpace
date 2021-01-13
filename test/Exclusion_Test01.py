# 爬取豆瓣电影喜剧评分数据
import requests
import json

if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list/'
    param = {'type': '24', 'interval_id': '100:90', 'action': '', 'start': '0', 'limit': '20'}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    response = requests.get(url=url, params=param, headers=headers)
    list_data = response.json()
    # 持久化分组 存储
    fp = open('./douban.json', 'w', encoding='utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False)
