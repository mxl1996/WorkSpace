# for 循环 遍历

# for
# 遍历字符串中每一个字母
name = 'xiaowang'
for n in name:
    print(n)
print("==============")
# 循环指定次数
count = 11
for c in range(count):
    print(c)
print("==============")
for i in range(count):
    if i == 4:
        continue
    elif i == 0:
        break
    print(i)

print("end")


