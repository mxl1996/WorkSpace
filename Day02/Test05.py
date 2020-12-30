# 如果为True 停止
"""
需要退出，让条件为False 或者 加break
"""
# count作用  计数器
# exit 捕获键盘输入，并且输出这个内容，当你输入的内容是exit，程序跳出
count = 1
while(count>0):
    print(count)
    count = count+1
    if count == 5:
        break
# range(5) 等同于[0,1,2,3,4]
for i in range(5):
    print(i)
# print(range(5))

while(True):
 s = input("是否退出:")
 if s=='exit':
     print("退出")
     break


