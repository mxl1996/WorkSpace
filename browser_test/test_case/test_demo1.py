# coding=utf-8
import time
import unittest

from browser_test.util.browser import Browser


class Demo1(unittest.TestCase):
    def setUp(self):
        self.browser = Browser.BROWSER
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_case1(self):
        u"""case1:访问百度首页"""
        browser = self.browser
        browser.get("https://www.baidu.com/")
        time.sleep(2)

    def test_case2(self):
        u"""case2:访问腾讯首页"""
        browser = self.browser
        browser.get("http://www.qq.com/")
        time.sleep(2)

    def test_case3(self):
        u"""case3:访问淘宝首页"""
        browser = self.browser
        browser.get("https://www.taobao.com/")
        time.sleep(2)

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
