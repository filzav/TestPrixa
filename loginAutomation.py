import unittest
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

url = "https://platform.kata.ai/login"
xpath_username = "//input[@placeholder='Username']"
xpath_password = "//input[@placeholder='Password']"
xpath_submit = "//button[@class='sc-kpOJdX hniTIz']"

class loginAutomation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_page_load_timeout(30)

    def test_login_success(self):
        driver = self.driver
        #1 Visit https://platform.kata.ai/login
        driver.get(url)
        self.assertIn('Kata Platform', self.driver.title)

        #2 Enter username, password
        username = driver.find_element_by_xpath(xpath_username)
        username.sendKeys('')
        password = driver.find_element_by_xpath(xpath_password)
        password.sendKeys('')
        driver.find_element_by_xpath(xpath_submit).click()

    def tearDown(self):
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()