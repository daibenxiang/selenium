from selenium import webdriver
import time
driver = webdriver.Firefox()
url = "http://tieba.baidu.com/"
driver.get(url)
driver.find_element_by_name("kw1").send_keys("hao")
time.sleep(3)
driver.quit()