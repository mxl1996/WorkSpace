
import requests
url ="http://v.juhe.cn/weather/ip"
# para = {"ip":"58.215.185.154","key":"221ec2c9d854d2859310ea808cb760fd"}
para = {"ip":"58.215.185","key":"221ec2c9d854d2859310ea808cb760fd"}
# 发送post请求
r = requests.post(url,data=para)
# 获取json数据
res = r.json()
print(res)
# print(res["reason"])
print(res["error_code"])