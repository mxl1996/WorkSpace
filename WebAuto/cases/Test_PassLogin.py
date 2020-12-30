import pytest

from WebAuto.common.Login import LoginAndCheck


# 数据驱动格式，测试数据与代码分离，以后增加新的测试用例，只需要修改数据就可
class Test_PassLogin:
    @pytest.mark.parametrize('username,password,expectedalert', [
        ('test01', 'a1b2c3d4', 'None')
    ])
    def test_UI_001(self, username, password, expectedalert):
        alertText = LoginAndCheck(username, password)
        assert alertText == expectedalert


if __name__ == '__main__':
    pytest.main()
