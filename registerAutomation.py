import unittest
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

url = "https://user.kata.ai/signup/"
xpath_username = "//input[@placeholder='Username']"
xpath_email = "//input[@placeholder='Email address']"
xpath_account_type = "//select[@placeholder='Select account type...']"
xpath_office = "//input[@placeholder='Company']"
xpath_school = "//input[@placeholder='School']"
xpath_captcha = '//*[@id="recaptcha-anchor"]/div[4]'
xpath_submit = "//button[@class='sc-gPEVay iwJPbg']"
xpath_error_username = "//div[@class='sc-TOsTZ jOCKoA']"
xpath_error_email = "//div[contains(text(),'Email is required.')]"
xpath_error_format_email = "//div[contains(text(),'Invalid email format.')]"
xpath_error_account_type = "//div[contains(text(),'Account type is required.')]"
xpath_error_office = "//div[contains(text(),'Company/School name is required.')]"

class registerAutomation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_page_load_timeout(30)

    def test_register_as_professional(self):
        driver = self.driver
        #1 Visit https://user.kata.ai/signup/
        driver.get(url)
        self.assertIn('Kata Platform', self.driver.title)

        #2 Enter username, email, choose Developers-Professional, and office
        username = driver.find_element_by_xpath(xpath_username)
        username.send_keys('asd')
        email = driver.find_element_by_xpath(xpath_email)
        email.send_keys('asd@asd.com')
        account_type_dropdown = driver.find_element_by_xpath(xpath_account_type)
        account_type = Select(account_type_dropdown)
        account_type.select_by_value('developers')
        office = driver.find_element_by_xpath(xpath_office)
        office.send_keys('asd')
        # For captcha, cannot be automated. The answers in here https://sqa.stackexchange.com/questions/17022/how-to-fill-captcha-using-test-automation number 2
        # wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,xpath_captcha))).click()
        driver.find_element_by_xpath(xpath_submit).click()

    def test_register_as_student(self):
        driver = self.driver
        #1 Visit https://user.kata.ai/signup/
        driver.get(url)
        self.assertIn('Kata Platform', self.driver.title)

        #2 Enter username, email, choose Developers-Student, and school
        username = driver.find_element_by_xpath(xpath_username)
        username.send_keys('asd')
        email = driver.find_element_by_xpath(xpath_email)
        email.send_keys('asd@asd.com')
        account_type_dropdown = driver.find_element_by_xpath(xpath_account_type)
        account_type = Select(account_type_dropdown)
        account_type.select_by_value('student')
        office = driver.find_element_by_xpath(xpath_school)
        office.send_keys('asd')
        # For captcha, cannot be automated. The answers in here https://sqa.stackexchange.com/questions/17022/how-to-fill-captcha-using-test-automation number 2
        # wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,xpath_captcha))).click()
        driver.find_element_by_xpath(xpath_submit).click()

    def test_register_failed_not_write_username(self):
        driver = self.driver
        #1 Visit https://user.kata.ai/signup/
        driver.get(url)
        self.assertIn('Kata Platform', self.driver.title)

        #2 Click username box but not write username
        driver.find_element_by_xpath(xpath_username).click()
        driver.find_element_by_xpath(xpath_email).click()
        wait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH,xpath_error_username), 'Username is required.'))

    def test_register_failed_write_username_less(self):
        driver = self.driver
        #1 Visit https://user.kata.ai/signup/
        driver.get(url)
        self.assertIn('Kata Platform', self.driver.title)

        #2 Write username but less than 3
        username = driver.find_element_by_xpath(xpath_username)
        username.send_keys('as')
        driver.find_element_by_xpath(xpath_email).click()
        wait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH,xpath_error_username), 'Username must be 3-15 characters long.'))

    def test_register_failed_not_write_email(self):
        driver = self.driver
        #1 Visit https://user.kata.ai/signup/
        driver.get(url)
        self.assertIn('Kata Platform', self.driver.title)

        #2 Click email box but not write email
        driver.find_element_by_xpath(xpath_email).click()
        driver.find_element_by_xpath(xpath_username).click()
        wait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH,xpath_error_username), 'Username is required.'))
        wait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH,xpath_error_email), 'Email is required.'))

    def test_register_failed_write_wrong_format_email(self):
        driver = self.driver
        #1 Visit https://user.kata.ai/signup/
        driver.get(url)
        self.assertIn('Kata Platform', self.driver.title)

        #2 Write email but with wrong format
        email = driver.find_element_by_xpath(xpath_email)
        email.send_keys('asd')
        driver.find_element_by_xpath(xpath_username).click()
        wait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH,xpath_error_username), 'Username is required.'))
        wait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH,xpath_error_format_email), 'Invalid email format.'))

    def test_register_failed_not_choose_account_type(self):
        driver = self.driver
        #1 Visit https://user.kata.ai/signup/
        driver.get(url)
        self.assertIn('Kata Platform', self.driver.title)

        #2 Click account type but not choose one of them
        driver.find_element_by_xpath(xpath_account_type).click()
        driver.find_element_by_xpath(xpath_username).click()
        wait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH,xpath_error_username), 'Username is required.'))
        wait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH,xpath_error_account_type), 'Account type is required.'))

    def test_register_failed_not_write_office(self):
        driver = self.driver
        #1 Visit https://user.kata.ai/signup/
        driver.get(url)
        self.assertIn('Kata Platform', self.driver.title)

        #2 Choose Developer - Professional but didn't write office
        account_type_dropdown = driver.find_element_by_xpath(xpath_account_type)
        account_type = Select(account_type_dropdown)
        account_type.select_by_value('developers')
        driver.find_element_by_xpath(xpath_office).click()
        driver.find_element_by_xpath(xpath_username).click()
        wait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH,xpath_error_username), 'Username is required.'))
        wait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH,xpath_error_office), 'Company/School name is required.'))

    def tearDown(self):
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()