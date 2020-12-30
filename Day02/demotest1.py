# 接收键盘输入内容
import random
# dashu_age = random.randint(10, 11)

# age = input("请输入年龄:")
# print("输入的年龄是", age)
# 比较的时候会出问题,需要强转一下类型
# int_age = int(age)
# print(int_age, type(int_age))
# if int_age == dashu_age:
#     print("猜对了")
# elif int_age > dashu_age:
#     print("猜大了")
# else:
#     print("猜小了")
# print("大叔的真实年龄是", dashu_age)

# 通过 for 循环实现 7次游戏结束后退出
count = 7
dashu_age = random.randint(10, 11)
for i in range(count):
    age = input("请输入年龄:")
    print("输入的年龄是", age)
    # 比较的时候会出问题,需要强转一下类型
    int_age = int(age)
    # print(int_age, type(int_age))
    if int_age == dashu_age:
        print("猜对了")
    elif int_age > dashu_age:
        print("猜大了")
    else:
        print("猜小了")
