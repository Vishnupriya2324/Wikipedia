import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import requests
import unittest
from pages.wikipediaPage import wikipediaPage


class SmokeTests(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="C:\\Users\\Dell\\PycharmProjects\\submit\\drivers\\chromedriver2.exe")
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("https://en.wikipedia.org/wiki/Selenium")


    def test_001_Wikipedia(self):

            driver = self.driver
            wp = wikipediaPage(driver)
            wp.verify_ExternalLinks()
            wp.isFeaturedArticle()
            wp.take_screenshot()
            wp.get_PDFCount()
            wp.verify_plutonium()


    @classmethod
    def tearDownClass(self):
        driver = self.driver

        self.driver.quit()





    if __name__ == '__main__':
        unittest.main()