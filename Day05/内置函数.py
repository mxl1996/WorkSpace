print(all([1,2,3,4]))# 判断可迭代的对象里面的值是否都为真
print(any([0,1,2,3,4]))# 判断可迭代的对象里面的值是否有一个为真
print(bin(10))# 十进制转二进制
print(bool('s'))# 把一个对象转换成布尔类型
print(bytearray('abcde',encoding='utf-8'))# 把字符串变成一个可修改的bytes
print(callable('aa'))# 判断传入的对象是否可调用
print(chr(10))# 打印数字对应的ascii
print(ord('b'))# 打印字符串对应的ascii码
print(dict(a=1,b=2))# 转换字典
print(dir(1))# 打印传入对象的可调用方法
print(eval('[]'))# 执行python代码，只能执行简单的，定义数据类型和运算
print(exec('def a():pass'))# 执行python代码
print(filter(lambda x:x>5,[12,3,12,2,1,2,35]))# 把后面的迭代对象根据前面的方法筛选
print(map(lambda x:x>5,[1,2,3,4,5,6]))
print(frozenset({1,2,3,3}))# 定义一个不可修改的集合
print(globals())# 返回程序内所有的变量，返回的是一个字典
print(locals())# 返回局部变量
print(hash('aaa'))# 把一个字符串哈希成一个数字
print(hex(111))# 数字转成16进制
print(max(111,12))# 取最大值
print(oct(111))# 把数字转换成8进制
print(round(11.11,2))# 取几位小数
print(sorted([2,31,34,6,1,23,4]))# 排序，默认是升序，sorted(s,reverse=True)
dic={1:2,3:4,5:6,7:8}
print(sorted(dic.items()))# 按照字典的key排序
print(sorted(dic.items(),key=lambda x:x[1]))# 按照字典的value排序
__import__('decorator')# 导入一个模块

# join 连接字符串
# ''.join(list)   以''内分割，例如list转化成字符串
# lambda 匿名函数 只能写简单的功能不能写复杂的
test = lambda  a,b:a+b  # 冒号前面是入参，冒号后面是返回值-
def test2(a,b):
    return a+b
# 拆包
score=[1,2,3]
name=["xiaohei","xiaobai"]
d={}
for index in range(len(name)):
    key=name[index]
    value=score[index]
    d[key]=value
print(d)
# name score 个数不一样 以最小的为准
print(list(zip(name,score)))


def zhaoduixiang(item):
    age = item.get("age")
    if age<25:
        return True

person = [
    {"name":"xiaoming2","age":23},
    {"name":"xiaoming3","age":24},
    {"name":"xiaoming4","age":25},
    {"name":"xiaoming5","age":26},
    {"name":"xiaoming6","age":27},
    {"name":"xiaoming7","age":28},
]
result=list(filter(zhaoduixiang,person))
print(result)
