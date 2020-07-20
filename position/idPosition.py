from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.get("http://www.cnblogs.com/yoyoketang/p/")
driver.forward()
time.sleep(3)
driver.refresh()
time.sleep(5)
driver.close()
time.sleep(3)
driver.quit()