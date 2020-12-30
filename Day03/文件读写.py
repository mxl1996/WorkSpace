# 文件读写(i/o)
# 怎么去读？
# 打开文件
# 读取内容
# 关闭文件


# 不在同一个路径下，要写相对路径，绝对路径
# 相对路径：../day03/a.txt  ./n.txt
# 绝对路径： /usr/local/nginx/n.txt
# 打开文件的时候，文件一定是要存在的
# file2=open("D:\\n.txt")
# 打开
# open打开的文件是一个流，
file = open("n.txt")
print(file)
# file.tell() 当前位置
# 跳到目标位置
# file.seek()
print(file.read())
print(file.readline())
print(file.readlines())
file.close()
file1=open("a.txt","w",encoding="utf-8")
data="天琴座"
# 写入数据分为 r w a(追加append)
file1.write(data)
l1=["xiaohong","xiaobai"]
file1.writelines(l1)
for l in l1:
    file1.write(l)
    file1.write("\n")
file1.close()