# 如何来定义一个变量

name = '张三'
name2 = "小王"
name3 = '''小李'''

print(name)
print(name2)
print(name3)

age = 18
age2 = "18"

print(age, type(age))
print(age2, type(age2))
agetype = type(age2)
print(age2, agetype)

# + ,
print(name + name2)
print(name, name2)
print(name, name2)
# print(name + age)
print(name, age)
# 小王今年18岁
print(name2 + '今年' + str(age))

print(age + int(age2))
print('''   我说:'大叔很"帅"'    ''')
print("大叔\"帅\"")

