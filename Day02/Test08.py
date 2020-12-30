# login 功能 结合list索引
# login 功能，用户输入用户名密码，进行登录

user_list =['00088880001', '00088880002','00088880003']
pwd_list = [123456,654321,132465]
# 让用户输入用户名、密码
# 判断用户名是否存在
# 如果用户存在，则校验他的密码是否正确
# 如果用户不存在，则不需要校验密码
# 附加功能： 实现 3次登录，失败后退出程序
# print(pwd_list.index(654321))
count =3
username=input("请输入用户名：")
password=input("请输入密码：")
for i in count:

   if user_list.count(username)>0:
       inde= user_list.index(username)
       if str(pwd_list[inde])==password:
        print("登录成功")
       else:
        print("密码错误")
        i=i+1

   else:
      print("用户名密码错误")
