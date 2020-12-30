# # # 字符串切片
# t='haha'
# print("t:",t)
# #  输出要查找内容出现的次数
# # print(t.count("a"))
# # print(t.count("b"))
# #  查找要找的内容片断，从左向右找第一个，就返回被找到内容的下标
# # print(t.find("a"))
# # print(t.find("hx"))
# # # 和find一样的形式，从左向右去找
# # print(t.index("a"))
# # #
# # un ="姓名:{name},年龄:{age}"
# # print(un.format(name="xiaoming",age=18))
# # # 把字典中的每个key和字符串中声明的站位去进行查找，format更灵活
# # print(un.format_map({"name":"xiaoming","age":18}))
#
# # 去除前后空格，但是不会去除字符串中间的空格
# print(" abc".strip())
# print("abc ".strip())
# print(" abc ".strip())
# print(" a b c ".strip())
#
# # 是否是空格
# s =" "
# s1=" 1"
# print(t.isspace())
# print(s.isspace())
# print(s1.isspace())
#
# # 判断是否是字符
# s="今天"
# d="123"
# # print(t.isalpha())
# # print(s.isalpha())
# # print(d.isalpha())
# # pwd = input("请输入6位数字密码:")
# # # 包含纯数字
# # if pwd.isalpha() :
# #     print("密码不是纯数字")
# # else:
# #     print("密码是纯数字")
# # 置为大写
# print(t.upper())
# # 使用场景，接收到用户输入的验证码，先做小写转换，在做比较
# # 置为小写
# print(t.lower())
# # split 重点
# f = "xiaowang,xiaoli,xiaobai,xiaohong"
# # f.split(",")
# # 将字符串转为list
# new_f=f.split(",")
# val = "这个学生的姓名是：xiaowang"
# for name in new_f:
#     print()
#
# print(f.replace(",", "\n"))
f = "xiaowang,xiaoli,xiaobai,xiaohong"
print(f.replace(",", "\n"))
new_f = f.split(",") # 切分
print(new_f)
new_f.reverse()  #反转
val = "这个学生的姓名是：{name}"
for name in new_f:
    print(val.format(name=name))



