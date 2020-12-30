# 欢迎 xx 登录，今天是xxxx年xx月xx日

name = "xiaowang"
year = 2020
m = 12
day = 20
# 字符串格式化的方式有哪种
# 第一种实现方式： 拼接字符串
print("欢迎" + name + "登录,今天是" + str(year) + "年" + str(m) + "月" + str(day) + "日")
# 第二种实现方式： %
print("欢迎%s登录,今天是%s年%s月%s日" % (name, year, m, day))
# 第三种实现方式: format
print("欢迎{name1}登录,{name1}今天是{y}年{m}月{d}日{name1}".format(name1=name, y=year, m=m, d=day))
data = "欢迎{name1}登录,今天是{y}年{m}月{d}日"
print(data.format(name1=name, y=year, m=m, d=day))

