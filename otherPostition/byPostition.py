from selenium.webdriver.common.by import By
from selenium import webdriver
import time
driver = webdriver.Firefox()

url = "http://www.baidu.com/"
driver.get(url)
# driver.find_element_by_class_name("s_ipt").send_keys("123")
# driver.find_element(By.CLASS_NAME, "s_ipt").send_keys(569)
# driver.find_element(By.ID, "kw")
# driver.find_element(By.NAME, "wd")
driver.find_elements_by_class_name("s_ipt")


time.sleep(3)
driver.quit()