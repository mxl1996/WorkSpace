s="http://www.limlhome.cn/bbs/forum.php"
n="123456789"
# s[起始：结束：步长]

# 如果只有起始，没有结束，则代表从起始位置到最后
print(s[7:])
# 如果只有结束，没有起始，则代表从0开始到结束点的前一个结束
print(s[:22])
# 如果左右区间都有设置，则输出指定内容
print(s[7:22])
# 如果需要跳一位输出，则设置步长
print(n)
print(n[::2])
print(n[1::2])
# 从后向前去推
print(n[:-1])
print(n[:-2])
print(n[-1])
# for 循环如何倒序输出
print(n[-1])
print(n[-2])
print(n[-3])