import random
import string

# 生成账号密码，账号必须包含字母和数字，长度在6-12之间
# 密码必须包含大小写字母，数字，特殊符号，长度在8-12之间
# 输入几，就产生几条，并且用户名不能重复

input_count=input("请输入产生的数据条数：").strip()
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation) #所有的特殊符号
print(string.ascii_letters) #大写字母+小写字母
if not input_count.isdigit():
    print("请输入整数")
else:
    input_count = int(input_count)
    def check_username(username):
        return set(username) &set(string.ascii_letters) and set(username)& set(string.digits)
for i in range(input_count):
    username_len=random.randint(6,12)
    username_list=random.sample(string.ascii_letters+string.digits,username_len)
    # 效验合法性
    if check_username(username_list):
        username=''.join((username_list))

    password_len=random.randint(8,12)






