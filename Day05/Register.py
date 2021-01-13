# 写文件
def write_file(filename, content):
    with open(filename, 'a') as fw:
        fw.write(content)


# 读文件
def read_file(filename):
    with open(filename, 'r') as fr:
        return fr.readlines()


user_list = []


# 获取已经存在的用户列表
def get_userinfo():
    for userinfo in read_file(filename='user.txt'):
        userinfo = userinfo.strip().split(',')[0]
        user_list.append(userinfo)
        return user_list


# 注册

def Register():
    for i in range(3):
        username = input("请输入用户名")
        password = input("请输入密码")
        repassword = input("请确认密码")
        if username in get_userinfo():
            print("用户名重复")
            continue
        elif len(username) < 6 or len(username) > 20:
            print("用户名长度需为6-20位字符")
        elif len(password) < 8 or len(password) > 15:
            print("密码长度为8-15个字符")
        elif password != repassword:
            print("两次密码不一致")
        else:
            print("恭喜注册成功")
            write_file('user.txt', ('\n'+username+','+password))
            break
    else:
        print("您输入错误次数已经超过三次")

if __name__ == '__main__':
    Register()