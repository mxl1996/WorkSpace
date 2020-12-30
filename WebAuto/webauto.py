from selenium import webdriver
import time
# webdriver 对象，操控浏览器
driver = webdriver.Chrome(r'D:\chromedriver.exe')
# wd.get("https://www.baidu.com")
driver.get('http://10.1.35.48:10000/sdar/#/login')

driver.find_element_by_id('username').send_keys("test0111")

driver.find_element_by_id('password').send_keys("a1b2c3d4")

driver.implicitly_wait(10)
time.sleep(10)
driver.find_element_by_css_selector('.login-button').click()
print(driver.find_element_by_css_selector('.login-button').text)
time.sleep(3)
print(driver.find_element_by_css_selector('.ant-notification-notice-description').text)







