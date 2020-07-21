from selenium import webdriver
import time
driver = webdriver.Firefox()

url = "http://www.baidu.com/"
driver.get(url)
driver.find_element_by_class_name("s_ipt").send_keys("123")
time.sleep(3)
driver.quit()