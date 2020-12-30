# nginx 日志监控
# 用来监控nginx 日志中记录的ip 当某一个ip出现次数超过50次以后，报警XX地址，已经访问超过50次
# 运行频率 每分钟运行一次
# 数据来源为： nginx的access.log  读取文件（I/O操作)


# 1、读取文件（I/O文件)，open(access.log)
import time
# while True:
#    file = open("access.log", encoding="utf-8")
#    ip_list=[]
#    for line in file:
#     ip = line.split(" ")[0]
#     print(ip)
#     ip_list.append(ip)
#     ip_set=set(ip_list)
#     print(ip_set)
#     for ip in ip_set:
#      print(ip,":",ip_list.count(ip))
#     if ip_list.count(ip)>=50:
#         print("{ip}已经出现超过50次，请及时确认是否存在风险".format_map(ip=ip))
#   file.close()
#   print("====结束===")
#   time.sleep(60)

# 2、解析文件，分析出ip
# 3、把ip存起来并且记录ip出现的次数
# 4、 分析记录的每个ip出现的次数，当某个ip出现次数超过50次，打印出这个ip出现次数超过50
# 5、让这个程序滚动起来，不会停止，监控，每分钟运行一次
# 6、当读取数据时，跳过已读数据，需要记录上次记录到哪了，下次读取的时候先先进行跳转
# 第二种方式，用字典去实现
ip_dict={}
while True:
    file = open("access.log", encoding="utf-8")
    # 解析文件 分析ip
    for line in file:
        ip=line.strip().split(" ")[0]
    # 