#导入包
import requests
#给接口地址定义变量名称
url="http://v.juhe.cn/weather/index"
#将参数定义成变量para
para={"cityname":"北京","key":"221ec2c9d854d2859310ea808cb760fd"}

#发送请求
#对应结果叫：r
r=requests.get(url,params=para)
print(r.status_code)

#获取json数据
print(r.json())
res=r.json()
print(res["reason"])
print(res["result"])
print(res["result"])
