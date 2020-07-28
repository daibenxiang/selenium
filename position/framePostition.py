from selenium import webdriver
driver = webdriver.Firefox()
url = "http://mail.126.com/"
driver.get(url)
driver.implicitly_wait(10)
frame = driver.find_element_by_xpath('//iframe[@id="x-URS-iframe"]')
driver.switch_to_frame(frame)
driver.find_element_by_name("email").send_keys("adb")
driver.find_element_by_name("password").send_keys("123")
driver.quit()