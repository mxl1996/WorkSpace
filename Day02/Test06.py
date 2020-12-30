"""
格式化
欢迎XX登录，今天是XXX年XX月XX日
"""
name ="xiaowang"
year = 2020
month = 12
day = 20
# 字符串格式化的方式有哪几种？
# 第一种实现方式：拼接字符串
print("欢迎"+name+"登录，今天是"+str(year)+"年"+str(month)+"月"+str(day)+"日")
# 第二种实现方式 %
print("欢迎%s登录,今天是%s年%s月%s日"%(name, year, month, day))
# 第三种实现方式 format
print("欢迎{n}登录，今天是{y}年{m}月{d}日".format(n=name,y=year,m=month,d=day))

