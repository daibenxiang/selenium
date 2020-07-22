from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
# context_click() 右击
# double_click() 双击
# drag_and_drop(source, target)拖动
# move_to_element() 鼠标悬停
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
# time.sleep(3)
# mouse = driver.find_element_by_xpath(".//*[@id='s-usersetting-top']")
# ActionChains(driver).move_to_element(mouse).perform()
# time.sleep(1)
# # 鼠标悬停后执行
# driver.find_element_by_link_text("搜索设置").click()
time.sleep(3)

# 导入ActionChains 类from selenium.webdriver.common.action_chains import ActionChains
# 定位元素的源位置
element = driver.find_element_by_name("tj_login")
# 定位元素要移动到的目标位置
target = driver.find_element_by_id("kw")
# 执行元素的拖放操作
ActionChains(driver).drag_and_drop(element, target).perform()
time.sleep(3)
driver.quit()
