# coding=utf-8
import time
import unittest

from browser_test.util.browser import Browser


class Demo2(unittest.TestCase):
    def setUp(self):
        self.browser = Browser.BROWSER
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_demo2_case1(self):
        u"""demo2_case1：访问携程"""
        browser = self.browser
        browser.get("http://www.ctrip.com/")
        time.sleep(2)

    def test_demo2_case2(self):
        u"""demo2_case2：访问QQ注册"""
        browser = self.browser
        browser.get("http://zc.qq.com/chs/index.html")
        time.sleep(2)

    def test_demo2_case3(self):
        u"""demo2_case3：访问百度贴吧"""
        browser = self.browser
        browser.get("http://tieba.baidu.com/")
        time.sleep(2)

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
