# list就是其他语言的数组
"""
list：有序可重复的
"""
a = [1,2,3,4,5,6,7,8,9,0]
print(a)
print(a)
# 打印每次顺序都是一样的
# 学习list的几个方面
# 增
l1 = []  # 创建空list
print(type(l1))
l2=[1,2,3,4,5,6,7,8,9,0,0]
# 添加到最后一个
l2.append(11)
print(l2)
# 下标处 2 插入12，向右移动
# list中每个元素他们所在位置id 叫做下标，这个id是从左向右开始数，由0开始数
l2.insert(2, 12)
print(l2)
# 删 remove删除通过值进行删除，从左向右数删除第一个找到的值
# 删除 如果不存在会报异常
# 如果有多个0 ，删除会是什么样呢？会默认删除第一个
# pop 删除通过索引 index，下标删除，同时 会把被删除的值返回
print(l2.remove(0))
print("------------------------------")
print(l2)
print(l2.pop(4))
# 改 通过索引id、下标替换值
l2[0]=100
print(l2)


# 查
print(l2[0])
print(l2[1])
# 扩展方法
print(l2.count(0))
# 判断某个数据是否在list中存在
if l2.count(0)>0:
    print("0存在于list中")
else:
    print("0不存在于list中")
# 遍历列表数据
for i in l2:
    print("当前元素为",i)

