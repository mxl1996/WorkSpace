import random
import json

user_list = ['1', '00088880002', '00088880003']
pwd_list = [1, 654321, 132465]
good_list = [{"name": "电脑", "price": 1999}, {"name": "鼠标", "price": 10}, {"name": "游艇", "price": 20}, ]
buycar = []
uname = input("请输入用户名:")
pwd = input("请输入密码:")
umoney = random.randint(100, 1000)
# 判断这个用户名在list中是否存在
if user_list.count(uname) > 0:
    inde = user_list.index(uname)
    if str(pwd_list[inde]) == pwd:
        print("登录成功")
        print("您当前可用金额为:", umoney)
        print("您当前可买的商品有", good_list)
        if umoney > 0:
            buygood = str(input("请输入您要买的商品:"))
            for i in good_list:
                if i["name"] == buygood:
                    print("您要买的商品是：", buygood)
                    buycar.append(buygood)
                    umoney = umoney - i["price"]
                    if umoney <= 0:
                        print("您当前所剩余额不足")
                        print("您当前剩余金额为", umoney)
                        add = str(input("请问是否继续充值，是请输入y，不充值输入n？"))
                        if add == "y":
                            add_money = int(input("您要充值的金额是："))
                            umoney = umoney + add_money
                            print("您充值后的金额是%d，您当前购物车的商品有%s，它的价格为%d" % (umoney, buycar,i["price"]))
                            exit()

                        else:
                           print("您当前消费金额为", i["price"])
                           print("您当前剩余金额为", umoney)
                           break
                else:
                    print("您输入的商品不合法，请检查商品列表")
    else:
        print("您会员卡所剩余金额不足")

else:
    print("用户名或密码错误")

