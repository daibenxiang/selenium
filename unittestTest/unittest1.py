from selenium import webdriver
import unittest
import time


class Baidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.baidu.com")

    def test_001(self):
        '''搜索selenium'''

        driver = self.driver
