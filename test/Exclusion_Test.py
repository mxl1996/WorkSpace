import requests

"""
爬虫与数据分析学习day01
爬虫：通过编写程序模拟浏览器上网，然后让其去互联网上抓取数据的过程
爬虫分类：通用爬虫（抓取系统重要组成部分，抓取的是一整张页面数据。）
         聚焦爬虫（抓取页面中特定的局部内容）
         增量式爬虫（只抓取网站中最新更新的数据）
"""
# res = requests.get('https://editor.csdn.net/md?articleId=109320746')
# novel=res.text
# #把Response对象的内容以字符串的形式返回
# #打开已经创建好的文件
# k = open('Test_Exc_Data.Text', 'a+')
# k.write(novel)
# #写进文件中
# k.close()
# #关闭文档

# 需求1：采集搜索后的网页数据
if __name__ == '__main__':
    # 1、指定url
    url = 'https://www.sogou.com/web'
    # 处理url携带的参数，封装到字典中
    kw = input('enter a word:')
    param = {'query': kw}
    # UA伪装：让爬虫对应请求载体身份标识伪装成某一款浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
# 2、对指定url发起请求，携带参数，并处理参数
response = requests.get(url=url, params=param,headers=headers)
# 3、获取数据
page_text = response.text
fileName = kw + '.html'
with open(fileName, 'w', encoding='utf-8') as fp:
    fp.write(page_text)
    print(fileName, '保存成功')
# UA检测：门户网站的服务器会检测对应请求的载体身份标识，如果检测请求的载体身份标识为某一款浏览器，说明该请求是个正常请求，但是如果检测请求载体的身份标识不是基于浏览器，则标识该请求为不正常请求（爬虫）

