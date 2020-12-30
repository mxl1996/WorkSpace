"""
if 小练习：判断年龄：
定义好大叔的年龄：随机数
接收键盘输入的年龄数，然后和大叔的年龄对比
如果输入的比大叔的年龄大或者小，则提示大或者小
如果输入的和大叔的年龄一致，则提示输入正确
"""
import random
age = input("请输入年龄：")
# 注意类型转换
int_age = int(age)
# 随机生成10-40之间的数字
dashu_age = random.randint(10, 40)
print("大叔的年龄是："+dashu_age)
if int_age > dashu_age:
    print("年龄大于随机年龄")
elif int_age == dashu_age:
    print("年龄与大叔年龄相等")
else:
    print("年龄小于大叔年龄")
"""
常见异常：TypeError：不同数据类型去做拼接处理
          ValueError：类型转换时，无法完成转换

"""
import random
count = 2
# 随机生成10-40之间的数字
dashu_age = random.randint(10, 40)
for i in range(count):
    age = input("请输入年龄：")
    int_age = int(age)
    if int_age > dashu_age:
        print("年龄大于随机年龄")
    elif int_age == dashu_age:
        print("年龄与大叔年龄相等")
        print(dashu_age)
        break
    else:
        print("年龄小于")




