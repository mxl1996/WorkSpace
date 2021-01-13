"""
聚焦爬虫
编码流程：
1、指定url
2、UA伪装
3、发起请求，参数处理
4、获取响应数据
5、数据解析
6、持久化存储
数据解析：
-xpath
-bs4
-正则
数据解析原理：
-解析的数据都在标签里，或者标签里对应的属性值中进行存储
步骤：1、指定标签的定位
     2、标签或者标签对应属性中存储的数据进行提取（解析）
"""
# 需求：爬取糗事百科的图片数据
import requests
import re
import os

if __name__ == '__main__':
    # 创建文件夹保存所有图片
    if not os.path.exists('./qiutuLibs'):
        os.mkdir('./qiutuLibs')
    url = 'https://www.qiushibaike.com/imgrank/'
    # 对应爬取所有页码的图片数据
    # https://www.qiushibaike.com/imgrank/page/13/
    # 设定一个通用的url的模板
    url1 = 'https://www.qiushibaike.com/imgrank/page/%d/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    for page_num in range(1, 3):
        new_url = format(url1 % page_num)
        print(new_url)

        # 使用聚焦爬虫，爬取所有图片
        # 如何从当前源码解析到image标签对应的src的值? 经过分析  抽取class=thumb
        page_text = requests.get(url=url1, headers=headers).text

        ex = '<div class="thumb">.*?<img src="(.*?)" alt=.*?</div>'
    # re.S 多行
        image_src_list = re.findall(ex, page_text, re.S)
    # print(image_src_list)
        for src in image_src_list:
        # 拼接出一个完整的图片url
          src = 'https:' + src
        # 获取二进制数据，请求到了图片的二进制数据
          image_data = requests.get(url=src, headers=headers).content
        # 进行持久化存储
        # 生成图片名称，截取图片地址中的名称
          src_name = src.split('/')[-1]
          imgPath = './qiutuLibs/' + src_name
          with open(imgPath, 'wb') as fp:
             fp.write(image_data)
             print('下载成功')

""" 
<div class="thumb">
<a href="/article/123931741" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/12393/123931741/medium/0KFTME2A94E5FQ3G.jpg" alt="糗事#123931741" class="illustration" width="100%" height="auto">
</a>
</div>
"""
