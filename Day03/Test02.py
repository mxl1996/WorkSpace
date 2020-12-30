# 什么场景下用纯数字做key
# 每个key为userid，
# 复杂类型变量定义规范
user_info ={}

# user_info[1001]={"name":"xiaoming","age":18}
# user_info[1002]={"name":"xiaobai","age":18}
# # print(user_info)
# # 增
user_list = ['00088880001', '00088880002', '00088880003']
pwd_list = [123456, 654321, 132465]
for i in user_list:
    inde = user_list.index(i)
    user_info[user_list[inde]] = pwd_list[inde]
    print(user_info)
# 查
# print(user_info.keys())
# print(user_info.items())
# print(user_info.values())
# print("====通过keys遍历=====")
# for i in user_info.keys():
#     print(i)
#     print(user_info[i])
# print("通过items遍历")
# for x in user_info.items():
#     print(x)
#     print(x[0],x[1])
# print("====两个变量循环===")
# for k,v in user_info.items():
#     print(k,v)
