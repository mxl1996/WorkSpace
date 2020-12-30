"""
题目1：有1、2、3、4个数字，
能组成多少个互不相同且无重复的数字的三位数，
输出这些数字和它的个数
"""
count = 0
n_list=[]
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and j != k and i != k:
                n = i * 100 + j * 10 + k
                #  print(n)
                n_list.append(n)
                count = count + 1

print("这些数字一共出现次数是：",count)
print("这些数字是：",n_list)

"""
题目2：一个整数，它加上100是一个完全平方数，加上268又是一个完全平方数，请问该数是多少
完全平方数? 一个数的平方根的平方=这个数本身，就是完全平方数
平方根的方法：sqrt
不知道对错，好像错了？？
"""
import math
i_list=[]
for i in range(1,100000):
    x=math.sqrt(i+100)
    y=math.sqrt(i+268)
    if x*x==i+100 and y*y==i+268:
        i_list.append(i)
print("这些数可能是？？",i_list)

"""
题目3：输入某年某月某日，判断这一天是这一年的第几天？
tm_yday：第几天
tm_wday:星期几

"""
import time
day=input("请输入今天的日期，example：yyyy-MM-dd：")
day_count=time.strptime(day,'%Y-%m-%d')
# 字符串格式化输出？
print("今天是今年的第%s天",day_count.tm_yday)

"""
题目4：输入三个数，从小到大输出
"""
list1=[]
for i in range(3):
    x=int(input('请输入数字进行排序:\n '))
    list1.append(x)
print("按顺序输出三个数：",sorted(list1))

"""
输出斐波那契数列的第n项
"""

"""
输出99乘法表

"""
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%2d '%(i,j,i*j),end='')
    print()
