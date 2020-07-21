from selenium import webdriver
import time
driver = webdriver.Firefox()
url = "http://www.baidu.com/"
driver.get(url)
driver.find_element_by_link_text("hao123").click()
#driver.find_element_by_partial_link_text("hao1").click()
time.sleep(3)
driver.quit()