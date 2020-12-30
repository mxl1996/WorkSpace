# 布尔类型
# true false
# if 对
# 否则
bool()
# 空字符串和长度为0的字符串
print(bool(None))
print(bool(""))
print(bool("1"))
# list 空和有参数
print(bool([]))
print(bool([1]))
# dict空和有参数
print(bool({}))
print(bool({"name":"zhangsan"}))
# 当变量，被赋予一个实际的值的时候，他一定是存在的，所以是true
# 当变量，没有赋值，他一定是不存在的，所以是false

user = input("请输入用户名：").strip()
if user:
    print("用户输入的内容是" ,user)
else:
    print("未输入")
