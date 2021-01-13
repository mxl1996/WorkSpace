"""
数据解析原理
-标签定位
-提取解析标签属性存储的数据值
bs4数据解析原理
-标签定位：1、实例化beautifulSoup对象，并且将页面源码数据加载到该对象中
          2、通过调用beautifulSoup对象中相关的属性或者方法进行标签定位和数据提取
"""

"""
    1、实例化的两种方法
     --将本地html文档加载到该对象中
    fp=open('./exclusion_bs4_test.html','r',encoding='utf-8')
    soup=BeautifulSoup(fp,'lxml')
    print(soup)
    -- 将互联网页面数据加载到对象中
    page_text=response.text
    soup=BeautifulSoup(page_text,'lxml')
    2、方法和属性
    -方法
    1）soup.tagName:返回的是文档中第一次出现的tagName的标签
    tagName：div...
    2)soup.find('div'):返回的是文档中第一次出现的div
      soup.find('div',class_/id/其他属性值='xx')定位class=xx/id=XX的div
    3)soup.findall()  返回符合要求的所有标签
    4)soup.select('某种选择器（id、class,标签选择器)'),返回的是一个列表
    5)层级选择器：soup.select('.xxxclassname>ul a')[i] >表示一个层级，空格表示多个层级
    -获取标签中文本数据、属性值
    1）soup.a标签.text、get_text()、string
    区别：前两个可以获取某一个标签中所有的文本内容，即使文本内容不属于该标签直系文本内容，而string只能获取该标签下直系的 文本内容
"""
from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
  # 需求：爬取三国演义小说所有章节标题和章节内容
  url='https://www.shicimingju.com/book/sanguoyanyi.html'
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
# 拿到页面数据
  html_text=requests.get(url=url,headers=headers).text
# 数据解析，bs4 解析
# 实例化 beautifulsoup对象
  soup=BeautifulSoup(html_text,'lxml')
  li_list=soup.select('.book-mulu>ul>li')
  fp=open('./sanguo.txt','w',encoding='utf-8')
  for li in li_list:
      # a标签直系文本内容，章节标题
      title=li.a.string
      print(title)
      detail_url='https://www.shicimingju.com'+li.a['href']
      # 对详情页发起请求，请求章节内容
      detail_page_text=requests.get(url=detail_url,headers=headers).text
      # 解析内容
      detail_soup= BeautifulSoup(detail_page_text, 'lxml')
      div_tag=detail_soup.find('div',class_='chapter_content')
      # 解析章节内容
      content=div_tag.text
      print(content)
      fp.write(title+':'+content+'\n')
      print(title,"爬取成功！")




