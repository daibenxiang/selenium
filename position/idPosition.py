from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
# driver.get("http://www.cnblogs.com/yoyoketang/p/")
driver.find_element_by_id("kw").send_keys("悠悠 博客")
# driver.forward() 左右键翻页
time.sleep(3)
# driver.refresh() 刷新页面
driver.find_element_by_id("su").click()  # 鼠标点击
time.sleep(5)
# driver.close() #关闭当前窗口
time.sleep(3)
driver.quit()