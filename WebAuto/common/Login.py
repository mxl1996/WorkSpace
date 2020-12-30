from selenium import webdriver
import time

# 重复调用登录，所以封装登录方法
def LoginAndCheck(username, password):
    driver = webdriver.Chrome(r'D:\chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('http://10.1.35.48:10000/sdar/#/login')
    if username is not None:
        driver.find_element_by_id('username').send_keys(username)
    if password is not None:
        driver.find_element_by_id('password').send_keys(password)

    driver.implicitly_wait(10)
    time.sleep(15)
    driver.find_element_by_css_selector('.login-button').click()
    time.sleep(3)
    alertText = driver.find_element_by_class_name('ant-notification-notice-description').text

    print(alertText)
    driver.quit()
    return alertText

