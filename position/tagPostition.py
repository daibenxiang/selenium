from selenium import webdriver
import time
driver = webdriver.Firefox()
url = "http://www.baidu.com/"
driver.get(url)
driver.find_element_by_tag_name("input").send_keys("hao")#标签会有多个 通常用于定位一组元素
time.sleep(3)
driver.quit()