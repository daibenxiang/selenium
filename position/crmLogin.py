from selenium import webdriver
import time
driver = webdriver.Firefox()
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


url = "http://139.196.82.174:8018"
driver.get(url)
driver.maximize_window()
time.sleep(4)
driver.find_element_by_xpath(".//*[@id='UserName']").send_keys("ben.dai@zhan.com")
driver.find_element_by_xpath(".//*[@id='section1']/form/div[2]/div/input").send_keys("111111")
driver.find_element_by_xpath(".//*[@id='code']").send_keys("888888")
time.sleep(2)
driver.find_element_by_xpath(".//*[@id='section1']/form/div[6]/div[1]/button").click()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='btnReset']").click()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='KeyWords']").send_keys("TPO202009110004009")
time.sleep(2)

driver.find_element_by_xpath(".//*[@id='searchWrap']/div[1]/span/button").click()

time.sleep(2)
'''报名按钮'''
driver.find_element_by_xpath(".//*[@id='clueInquireTable']/tbody/tr/td[3]/div/button[5]").click()
time.sleep(4)
'''下一步'''
driver.find_element_by_xpath("html/body/div[40]/div/div/div[3]/button[3]").click()
time.sleep(4)
'''选择课程类型'''
Select(driver.find_element_by_xpath(".//*[@id='maincontent']/div/div/div[2]/form/div/div[2]/div[2]/select")).select_by_index(1)

time.sleep(2)
'''选择科目'''
Select(driver.find_element_by_xpath(".//*[@id='maincontent']/div/div/div[2]/form/div/div[2]/div[3]/select")).select_by_index(3)
time.sleep(2)
'''选产品大类'''
Select(driver.find_element_by_xpath(".//*[@id='maincontent']/div/div/div[2]/form/div/div[2]/div[4]/select")).select_by_index(2)
time.sleep(2)
'''点击添加产品'''

driver.find_element_by_xpath(".//*[@id='maincontent']/div/div/div[2]/form/div/div[3]/h4/button").click()
time.sleep(4)
'''选择一个产品'''
elent=driver.find_element_by_xpath("html/body/div[42]/div/div/div[2]/table/tbody/tr[1]/td[2]")
ActionChains(driver).double_click(elent).perform()

# time.sleep(2)
# '''点击确定'''
# driver.find_element_by_xpath("html/body/div[42]").click()
time.sleep(3)
'''启用折扣'''
driver.find_element_by_xpath("//*[@id='maincontent']/div/div/div[2]/form/div/div[6]/div[1]/label").click()
time.sleep(2)
'''选择一个折扣'''
Select(driver.find_element_by_xpath(".//*[@id='maincontent']/div/div/div[2]/form/div/div[6]/div[1]/select")).select_by_index(4)
time.sleep(3)
'''下一步'''
driver.find_element_by_xpath("html/body/div[40]/div/div/div[3]/button[3]").click()

time.sleep(2)
'''支付主体'''
Select(driver.find_element_by_xpath(".//*[@id='maincontent']/div/div/div[3]/form/div/table/tbody/tr[1]/td[2]/select")).select_by_index(1)
time.sleep(2)
'''支付方式'''
Select(driver.find_element_by_xpath(".//*[@id='maincontent']/div/div/div[3]/form/div/table/tbody/tr[2]/td[2]/select")).select_by_index(2)
time.sleep(2)
'''支付渠道'''
Select(driver.find_element_by_xpath(".//*[@id='maincontent']/div/div/div[3]/form/div/table/tbody/tr[3]/td[2]/select")).select_by_index(3)
time.sleep(1)
'''支付金额'''
driver.find_element_by_xpath(".//*[@id='maincontent']/div/div/div[3]/form/div/table/tbody/tr[4]/td[2]/input").send_keys("999")
time.sleep(1)
'''付款账号'''
driver.find_element_by_xpath(".//*[@id='maincontent']/div/div/div[3]/form/div/table/tbody/tr[5]/td[2]/input").send_keys("dbx自动化")
time.sleep(3)
'''下一步'''
driver.find_element_by_xpath("html/body/div[40]/div/div/div[3]/button[3]").click()
time.sleep(3)
'''下一步'''
driver.find_element_by_xpath("html/body/div[40]/div/div/div[3]/button[3]").click()
time.sleep(3)
'''保存订单信息'''
driver.find_element_by_xpath("html/body/div[40]/div/div/div[3]/button[4]").click()
driver.quit()

