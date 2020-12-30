# 字符串处理

log = '223.104.3.169 - - [03/Jul/2020:17:09:31 +0800] "GET /bbs/forum.php HTTP/1.1" 404 1045 "-" "Apache-HttpClient/4.5.10 (Java/1.8.0_201)"'
ip=log.split(" ")

print(ip[0])

# 判断字符串是否以我输入的开始 输入的结束
t='haha'
print(t.startswith("h"))
print(t.endswith("h"))
print(t.endswith("b"))

t.rsplit()
t.lstrip()