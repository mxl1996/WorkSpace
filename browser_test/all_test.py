# -*- coding:utf-8 -*-
"""
测试执行文件，执行test_case文件夹下的所有testcase
注意：只执行名称以test开头的py文件
"""
import os
import time
import unittest

from selenium import webdriver

from browser_test.util.HTMLTestRunner import HTMLTestRunner
from browser_test.util.browser import Browser

# 测试前打开浏览器
Browser.BROWSER = webdriver.chrome()

# 创建测试套件：discover()将所有test*.py加入套件
test_dir = os.getcwd()
testsuite = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py', top_level_dir=None)

# 执行测试套件，并使用HTMLTestRunner生成测试报告
ISOTIMEFORMAT = '%Y-%m-%d-%H-%M-%S'
time_str = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
filename = os.getcwd() + r'\test_report\result' + time_str + r'.html'
fp = open(filename, 'wb')
runner = HTMLTestRunner(stream=fp, title="TestDemo测试报告", description="用例执行情况：")
runner.run(testsuite)
fp.close()

# 测试结束，退出浏览器
Browser.BROWSER.quit()

