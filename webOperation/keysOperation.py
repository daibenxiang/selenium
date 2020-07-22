from selenium import webdriver
import time
# 导入Keys 模块
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
# 输入框输入内容
driver.find_element_by_id("kw").send_keys("seleniumm")
time.sleep(3)
# 删除多输入的一个m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
time.sleep(3)
# 输入空格键+“教程”
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
time.sleep(3)
driver.find_element_by_id("kw").send_keys(u"教程")
time.sleep(3)
# ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')
time.sleep(3)
# ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')
time.sleep(3)
# ctrl+v 粘贴内容到输入框
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')
time.sleep(3)
driver.quit()