from selenium import webdriver
import time
driver = webdriver.Firefox()
url = "http://www.baidu.com/"
driver.get(url)
driver.find_element_by_xpath(".//*[@id='kw']").send_keys("哈哈哈")
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='su']").click()
time.sleep(3)
driver.quit()