import requests

# 定义接口地址
url = "http://v.juhe.cn/weather/uni"
# para = {"key":"221ec2c9d854d2859310ea808cb760fd"}
para = {"key":"221ec2c9d854d2859310ea808cb760"}
# 发送接口请求
r = requests.get(url,params=para)
# 获取json数据
res = r.json()

# print(res)
# print(res["resultcode"])
print(res["error_code"])