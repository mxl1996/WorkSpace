# list 就是其他语言的数组
# 有序、可重复的
#
# 如何创建一个list
l1 = []  # 创建的空list 初始化
print(type(l1))
print(l1)
l2 = [1, 2, 3, 0, 4, 5, 6, 7, 8, 9, 0, 0, 0]
print(l2)
# 增
# 添加到最后一个，使用append
l2.append(10000001)
print(l2)
# 添加到指定位置, insert( 插到第几个，插入什么数据） 其他数据会向右挪一个位置
# list中每个值，他们所在位置的id 叫做 下标，这个id是从左向右由0开始数，
l2.insert(2, 12)
print(l2)
l2.insert(2, 13)
print(l2)
# 删
# remove 删除的时候通过值进行删除,从左向右数删除第一个找到的值
# 如果这个值不存在，会报异常
# pop 删除通过索引index/ 下标删除，同时会把被删除的值返回。
print("=================")
print(l2.remove(0))
# l2.remove(20)
print(l2)
print(l2.pop(4))
print(l2)
print("================")
# 改
# 通过索引id/下标 直接替换值
l2[0] = 100
print(l2)
print("=================")
# 查
print(l2[0])
print(l2[1])
print(l2[3])
# 扩展方法
print("====================")
print(l2)
print(l2.count(0))
print(l2.count(10))
# 判断 某个数据是否在list中存在

if l2.count(0) > 0:
    print("0 存在与list中")
else:
    print("0不存在于list中")
print("================================")
print(" =======开始遍历list =========")
# 遍历列表数据
for ii in l2:
    print("当前元素为：", ii)
# [100, 2, 13, 12, 4, 5, 6, 7, 8, 9, 0, 0, 0, 10000001]
