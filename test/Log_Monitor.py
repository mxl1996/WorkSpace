"""
需求：
nginx日志监控系统
数据来源为： nginx的access.log
当某一个ip出现次数超过50次以后
报警 xxxx 地址，已经访问超过50次  print
运行频率，每分钟运行一次

"""
import time
#  第一种方式，通过list实现
while True:
    ip_list = []
    # 1、读取文件（I/O操作）
    file = open("access.log", encoding="utf-8")
    # 2、解析文件，分析出ip
    for line in file:
        ip = line.strip().split(" ")[0]
        # 3、把ip存起来，并且记录ip出现次数
        ip_list.append(ip)
    # 去重
    ip_set = set(ip_list)
    # 4、分析记录到每个ip出现次数，当某一个ip出现次数超过50次，打印出 这个ip出现次数超过50次了
    for ip in ip_set:
        if ip_list.count(ip) >= 50:
            print("{ip} 已经出现了超过50次，请及时确认是否存在风险".format(ip=ip))
        print(ip, ":", ip_list.count(ip))
    file.close()
    print("=========结束本次=========")
    time.sleep(5)

# 第二种方式，通过dict 和 file的游标来实现的方式，增量读取解决读取文件的性能问题
ip_dict = {}
point = 0

while True:
    # 1、读取文件（I/O操作）
    file = open("access.log", encoding="utf-8")
    # 跳转到上一次记录到位置，如果是第一次则记录的位置是文件开始处
    file.seek(point)
    # 2、解析文件，分析出ip
    for line in file:
        # 从log中取出ip
        ip = line.strip().split(" ")[0]
        # 3、把ip存起来，存到一个字典，并且记录ip出现次数
        # 存储的容器可以是list，可以是dict，需要考虑是否要清空
        # 如果清空则每次全量读取
        # 如果不清空则每次要加入增量，不然能把重复数据加入
        #   这个地方就需要每次读取的时候跳到上次结束位置，所以不清空的模式需要用seek和tell

        # 字典计数器的功能，每个key就是一个ip ，值是ip的出现次数
        if ip_dict.get(ip):  # 非空即真 如果字典中之前记录过该ip，则记录的次数+1
            ip_dict[ip] += 1  # a += 1  等同于  a = a + 1
        else:  # 如果之前未记录，则初始化一个记录次数，初始化的值：1
            ip_dict[ip] = 1

    # 读取文件完成以后，记录一下这一次读取到哪里了，方便下一次seek到当前点
    point = file.tell()
    # 4、分析记录到每个ip出现次数，当某一个ip出现次数超过50次，打印出 这个ip出现次数超过50次了
    for key, value in ip_dict.items():
        if value >= 50:
            print("ip:%s,已经超出50次" % key)
    file.close()
    print("当前记录信息未：%s" % ip_dict)
    print("=========结束本次=========")
    time.sleep(5)
