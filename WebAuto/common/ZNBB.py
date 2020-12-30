from selenium import webdriver
import time
from WebAuto.cases import Test_PassLogin


def Login(self):
    driver = webdriver.Chrome(r'D:\chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('http://10.1.35.48:10000/sdar/#/login')
    driver.find_element_by_id('username').send_keys('test01')
    driver.find_element_by_id('password').send_keys('a1b2c3d4')
    driver.implicitly_wait(10)
    time.sleep(15)
    driver.find_element_by_css_selector('.login-button').click()
    time.sleep(3)
