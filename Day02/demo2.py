a = 2

if a > 1:
    print("a > 1")  # 判断如果成立进入这个print
else:  # 如果不成立则 进入这个else 逻辑里
    print("a <= 1")

if a > 1:
    a = a + 1
print("a:", a)

b = 1
if b > 1:
    print("b>1 ")
elif b == 1:
    print("b=1")
else:
    print("b<1")

# 身份证实名制判断
age = 28
'''
      题目：判断是否已经填写年龄的逻辑 按照 age > 0
                如果已经填写年龄：
                    输出已填写
                    if
                    else
                否则：
                    输出没有填写

'''
if age > 0:
    print("已填写年龄")
    if age >= 18:
        print("已成年")
    else:
        print("未成年")
else:
    print("未填写年龄")
print("==========================")
age2 = None
if age2:
    print("已填写年龄")
    if age >= 18:
        print("已成年")
    else:
        print("未成年")
else:
    print("未填写年龄")


if age2 is not None:
    print("已填写年龄")
    if age >= 18:
        print("已成年")
    else:
        print("未成年")
else:
    print("未填写年龄")

