import unittest
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://platform.kata.ai/login'
xpath_username = "//input[@placeholder='Username']"
xpath_password = "//input[@placeholder='Password']"
xpath_submit = "//button[@class='sc-kpOJdX hniTIz']"
xpath_remember = '//*[@id="remember-me"]'
xpath_forgot = "//a[contains(text(),'Forgot password?')]"
xpath_register = "//a[@class='text-bold']"
xpath_homepage = "//a[contains(text(),'Kata.ai')]"
xpath_errorLogin = "//div[@class='sc-dVhcbM diJyZz']"
xpath_tutorial = "//a[contains(text(),'See Tutorial')]"
xpath_docs = "//a[contains(text(),'View Docs')]"

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
        username.send_keys('hakermusic')
        password = driver.find_element_by_xpath(xpath_password)
        password.send_keys('buattestprixa')
        driver.find_element_by_xpath(xpath_submit).click()

    def test_login_success_with_remember_me(self):
        driver = self.driver
        #1 Visit https://platform.kata.ai/login
        driver.get(url)
        self.assertIn('Kata Platform', self.driver.title)

        #2 Enter username, password, click remember me
        username = driver.find_element_by_xpath(xpath_username)
        username.send_keys('hakermusic')
        password = driver.find_element_by_xpath(xpath_password)
        password.send_keys('buattestprixa')
        driver.find_element_by_xpath(xpath_remember).click()
        driver.find_element_by_xpath(xpath_submit).click()

    def test_go_to_forgot_password_page(self):
        driver = self.driver
        #1 Visit https://platform.kata.ai/login
        driver.get(url)
        self.assertIn('Kata Platform', self.driver.title)

        #2 Go to forgot password page
        driver.find_element_by_xpath(xpath_forgot).click()

    def test_go_to_register_page(self):
        driver = self.driver
        #1 Visit https://platform.kata.ai/login
        driver.get(url)
        self.assertIn('Kata Platform', self.driver.title)

        #2 Go to register page
        wait(driver, 50).until(EC.element_to_be_clickable((By.XPATH,xpath_register))).click()

    def test_go_to_homepage(self):
        driver = self.driver
        #1 Visit https://platform.kata.ai/login
        driver.get(url)
        self.assertIn('Kata Platform', self.driver.title)

        #2 Go to Kata.ai homepage
        wait(driver, 50).until(EC.element_to_be_clickable((By.XPATH,xpath_homepage))).click()

    def test_login_failed_wrong_username(self):
        driver = self.driver
        #1 Visit https://platform.kata.ai/login
        driver.get(url)
        self.assertIn('Kata Platform', self.driver.title)

        #2 Enter wrong username and password
        username = driver.find_element_by_xpath(xpath_username)
        username.send_keys('hakermusic')
        password = driver.find_element_by_xpath(xpath_password)
        password.send_keys('aaaaaaaaaaaa')
        driver.find_element_by_xpath(xpath_submit).click()
        wait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH,xpath_errorLogin), 'Invalid username or password'))


    def test_login_failed_wrong_username_and_password(self):
        driver = self.driver
        #1 Visit https://platform.kata.ai/login
        driver.get(url)
        self.assertIn('Kata Platform', self.driver.title)

        #2 Enter wrong username and password
        username = driver.find_element_by_xpath(xpath_username)
        username.send_keys('aaaaaaaaaaaa')
        password = driver.find_element_by_xpath(xpath_password)
        password.send_keys('aaaaaaaaaaaa')
        driver.find_element_by_xpath(xpath_submit).click()
        wait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH,xpath_errorLogin), 'Invalid username or password'))

    def test_go_to_tutorial_page(self):
        driver = self.driver
        #1 Visit https://platform.kata.ai/login
        driver.get(url)
        self.assertIn('Kata Platform', self.driver.title)

        #2 Click See Tutorial button
        wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,xpath_tutorial))).click()

    def test_go_to_docs_page(self):
        driver = self.driver
        #1 Visit https://platform.kata.ai/login
        driver.get(url)
        self.assertIn('Kata Platform', self.driver.title)

        #2 Click See Tutorial button
        wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,xpath_docs))).click()


    def tearDown(self):
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()