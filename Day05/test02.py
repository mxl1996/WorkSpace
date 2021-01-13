# li = [1,1,2,3,4,5,6,7,8,9]
# for i in li:
#     if i%2!=0:
#         li.remove(i)
# print(li)
# 输出结果 {1,2,4,6,8]
# 循环是循环 删除是删除，l3没动过
li = [1,1,2,3,4,5,6,7,8,9]
l3=[1,1,2,3,4,5,6,7,8,9]
for i in l3:
    if i%2!=0:
        li.remove(i)
print(li)
# 输出结果[2,4,6,8]
# 深拷贝 浅拷贝
li = [1,1,2,3,4,5,6,7,8,9]
# 浅拷贝，深拷贝list之间不相互影响
l3=li.copy()
print(id(li))
print(id(l3))
# 内存地址不一样也有可能是浅拷贝
import copy
# 深拷贝
l3=copy.deepcopy(li)