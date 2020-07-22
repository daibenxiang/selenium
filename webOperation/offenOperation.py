from selenium import webdriver
import time
driver = webdriver.Firefox()
url = "http://mail.126.com/"
driver.get(url)
time.sleep(3)
# driver.switch_to_frame("x-URS-iframe")\
# 清空输入框信息
# driver.find_element_by_name("email").clear()
# driver.find_element_by_name("email").send_keys("yefengrun")
# driver.find_element_by_name("password").send_keys("benxiang527080..")
# time.sleep(3)
driver.find_element_by_id("dologin").click()
# 也可以通过submit()模拟回车键(这里回车时候，光标是在密码框时候回车的)
driver.find_element_by_name("password").submit()
time.sleep(3)
driver.quit()