import pytest
import allure
import os

from WebAuto.common.Login import LoginAndCheck


# 数据驱动格式，测试数据与代码分离，以后增加新的测试用例，只需要修改数据就可
@allure.feature('登录错误信息验证功能')  # 用feature说明产品需求
class Test_ErrorLogin:
    @allure.story('错误账号登录')  # 用feature描述用户场景
    @pytest.mark.parametrize('username,password,expectedalert', [
        ('test088', 'a1b2c3d4', '用户test088不存在'),
        ('admin', 'a1b2c3d4', 'admin密码验证失败')
    ])
    def test_UI_001(self, username, password, expectedalert):
        alertText = LoginAndCheck(username, password)

        print("====测试登录失败第一条用例====")
        assert alertText == expectedalert


if __name__ == '__main__':
    pytest.main(['-v', '-s'])
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    pytest.main(['--alluredir', './temp'])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system('allure generate ./temp -o ./report --clean')
