# 爬数据练习
"""
1、解析数据
BeautifulSoup('要解析的数据‘，’解析器‘）
注意：要解析的数据必须是字符串、用参数来标识解析器：html.parser
2、提取数据
BeautifulSoup对象.findall(标签，属性）
BeautifulSoup对象.find(标签，属性）


"""
import requests # 调用requests库
from bs4 import BeautifulSoup # 调用BeautifulSoup库
res =requests.get('https://mp.weixin.qq.com/s?__biz=MzI4NDY5Mjc1Mg==&mid=2247489783&idx=1&sn=09d76423b700620f80c9da9e4d8a8536&chksm=ebf6c088dc81499e3d5a0febeb67fec27ba52f233b6a0e6fda37221a2c497dee82f2de29e567&scene=21#wechat_redirect')
# 返回一个response对象，赋值给res
html=res.text
# 把res解析为字符串
soup = BeautifulSoup( html,'html.parser')
# 把网页解析为BeautifulSoup对象
items = soup.find_all(class_='rich_media')   # 通过匹配属性class='rich_media'提取出我们想要的元素
for item in items:                      # 遍历列表items
    kind = item.find('h2')               # 在列表中的每个元素里，匹配标签<h2>提取出数据
    title = item.find(class_='profile_container')     #  在列表中的每个元素里，匹配属性class_='profile_container'提取出数据
    print(kind.text,'\n',title.text) # 打印书籍的类型、名字、链接和简介的文字

