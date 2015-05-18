# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class LoginForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.nba.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login_form(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        self.assertEqual("NBA.com", driver.title)
        driver.find_element_by_link_text("Login").click()
        # this will check  username is present 
        self.assertTrue(self.is_element_present(By.ID, "nbaLoginId"))
        driver.find_element_by_id("nbaLoginId").clear()
        driver.find_element_by_id("nbaLoginId").send_keys("admin")
        # this will check password is present
        self.assertTrue(self.is_element_present(By.ID, "nbaLoginPassword"))
        driver.find_element_by_id("nbaLoginPassword").clear()
        driver.find_element_by_id("nbaLoginPassword").send_keys("demo1234")
        # check forgot password link present
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Forgot Password?"))
        # check get sarted button is present
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#nbaAANewUser > a.nbaButton > span"))
        # check login with facebook button is present
        self.assertTrue(self.is_element_present(By.ID, "fb-auth"))
        # check login button is present on the form
        self.assertTrue(self.is_element_present(By.ID, "nbaLoginSubmit"))
        driver.find_element_by_id("nbaLoginSubmit").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
