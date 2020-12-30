# a = 1
# if a>1 :
#     print("a>1") # 判断如果成立进入这个print
# else :
#     print("a<=1") # 如果不成立 则进入else逻辑里
# if a>1:
#     a=a+1
# print("a:",a)
# b =1
# if b>1:
#     print("b>1")
# elif b==1:
#     print("b=1")
# else:
#     print("b<1")

# None 空
age = 28
age2 = None
if age>0:
    print("已填写年龄")
    if age>=18:
        print("已成年")
    else:
        print("未成年")
else:
    print("未填写年龄")
print("---------------------")

# 判断参数是否存在
if age2 is not None:
# if age2:
    print("已填写年龄")
    if age>=18:
        print("已成年")
    else:
        print("未成年")
else:
    print("未填写年龄")
