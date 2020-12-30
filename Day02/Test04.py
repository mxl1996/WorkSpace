"""
循环:遍历数据，遍历字典
for
continue  继续循环
break 直接跳出循环

where循环 条件循环
程序语言全部都是从0开始
"""
name = 'xiaowang'
for n in name:
    print(n)
print("-------------------")
# 循环指定次数
count = 10
for c in range(count):
    print(c)
print("-----------")
# 为什么执行结果没有4呢？if i==4 continue 继续进行循环，但是不会继续执行continue下面的逻辑，break直接跳出
for i in range(count):
    if i == 4:
        continue
    elif i == 6:
        break
    print(i)
