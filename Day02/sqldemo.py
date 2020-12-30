insert_sql = "insert into `user`(telephone,username,age,address) values"

sql_body = ""

# insert into `user`(telephone,username,age,address) values
# ('15900000001','xiaowang',24,'beijing'),
# ('15900000001','xiaowang',24,'beijing'),
# ('15900000001','xiaowang',24,'beijing');


tel = 15900000001
uname = '自动化用户_10'
age = 18
address = 'beijing'
address_list = ['bj', 'sh', 'tj']  # 可以随机取
for i in range(10):
    sql_body1 = "('%s','%s',%s,'%s')" % (tel + i, uname + str(i), age, address)
    sql_body = sql_body + sql_body1 + ","
    # print(sql_body)

# 拼接sql头和body，生成一个完整的sql语句
# print(insert_sql + sql_body)
# 字符串拼接，重新赋值
val = "张三" + "今年18岁"
print(val)
val = val + ",他很开心"
print(val)

# '''
# insert into `user`(telephone,username,age,address) values
# ('15900000001','xiaowang0',18,'beijing'),
# ('15900000002','xiaowang1',18,'beijing'),
# ('15900000003','xiaowang2',18,'beijing'),
# ('15900000004','xiaowang3',18,'beijing'),
# ('15900000005','xiaowang4',18,'beijing'),
# ('15900000006','xiaowang5',18,'beijing'),
# ('15900000007','xiaowang6',18,'beijing'),
# ('15900000008','xiaowang7',18,'beijing'),
# ('15900000009','xiaowang8',18,'beijing'),
# ('15900000010','xiaowang9',18,'beijing');
# '''
