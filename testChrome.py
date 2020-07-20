from selenium import webdriver
driver = webdriver.Chrome() #打开谷歌浏览器
driver.get("https://www.baidu.com")
driver.quit()