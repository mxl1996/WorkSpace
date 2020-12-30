import requests
#引用requests库
"""
爬虫与数据分析学习day01
"""
res = requests.get('https://editor.csdn.net/md?articleId=109320746')
novel=res.text
#把Response对象的内容以字符串的形式返回
# 打开已经创建好的文件
k = open('Test_Exc_Data.Text', 'a+')
k.write(novel)
#写进文件中
k.close()
#关闭文档
