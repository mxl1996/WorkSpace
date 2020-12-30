import random

insert_sql = "insert into `user`(telephone,username,age,address) values"
sql_body = ""
tel = 15900000001
uname = '自动化用户_10'
age = 18
address = 'beijing'
# 可以随机取
address_list = ['河北省', '山西省', '内蒙古', '辽宁省', '吉林省', '黑龙江省', '江苏省', '浙江省', '合肥市', '福建省', '江西省', '山西省', '山东省', '河南省',
                '湖北省']

for i in range(1000):
    # 循环随机取省份地址
    for j in range(15):
        sql_body1 = "('%s','%s',%s,'%s')" % (tel + i, uname + str(i), age, address_list[random.randint(1, 14)])
        # sql body拼接
        sql_body = sql_body + sql_body1 + ","
# 拼接sql头和body，生成一个完整的sql语句
print(insert_sql + sql_body)
