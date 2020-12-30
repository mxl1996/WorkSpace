# login功能，结合list的索引
# login功能，用户输入用户名密码，来进行登录

user_list = ['00088880001', '00088880002', '00088880003']
pwd_list = [123456, 654321, 132465]

# 让用户输入用户名、密码
# 判断用户名是否存在
# 如果用户存在，则校验他的密码是否正确
# 如果用户不存在，则不需要校验密码
# 附加功能： 实现 3次登录，失败后退出程序
# print(pwd_list.index(654321111))
# 获取用户名密码，从键盘输入
uname = input("请输入用户名:")
pwd = input("请输入密码:")
# 判断这个用户名在list中是否存在
if user_list.count(uname) > 0:
    inde = user_list.index(uname)
    print(inde)
    if str(pwd_list[inde]) == pwd:
        print("登录成功")
    else:
        print("用户名或密码错误")
else:
    print("用户名或密码错误")








