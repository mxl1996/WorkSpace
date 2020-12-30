# 导包
import requests
import re
#接口地址
url2 = "http://192.168.103.106:1080/webtours/nav.pl?in=home"
# 为了保持和下一个接口建立相同的连接通道
s = requests.session()
# 发送请求，传递url2
res = s.get(url2)
# 获取响应，运行检查该响应有没有实时的去获取userSession这个值
# print(res.text)
# 打印中数据观察<input type=hidden name=userSession value=OAA
# 通过正则匹配来获取，首先导入re包，r'要匹配的内容'，在哪个文件里匹配
usersession = re.findall(r'name=userSession value=(.+?)>', res.text)
# 打印，观察取第几个数据
print(usersession)
# 可以单独写也可以放在url中
# para2 ={"in":"home"}
# 接口地址
url ="http://192.168.103.106:1080/webtours/login.pl"
para ={"userSession":usersession[0],"username":"jojo","password":"bean","login.x":"54","login.y":"11","login":"Login","JSFormSubmit":"off"}
r = s.post(url,data=para)
# 发送post请求
# r = requests.post(url,data=para)
print(r.text)