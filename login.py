import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SmartxLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_correct_login(self):
        driver = self.driver
        driver.get("http://localhost:8080/SmartX/login")
        self.assertIn("Login", driver.title)
        # email
        elem_email = driver.find_element_by_name("email")
        elem_email.send_keys("internet@gmail.com")
        # password
        elem_pass = driver.find_element_by_name("senha")
        elem_pass.send_keys("123456")
        elem_pass.send_keys(Keys.RETURN)
    
    def test_wrong_login(self):
        driver = self.driver
        driver.get("http://localhost:8080/SmartX/login")
        self.assertIn("Login", driver.title)
        # email
        elem_email = driver.find_element_by_name("email")
        elem_email.send_keys("loremsup@gmail.com")
        # password
        elem_pass = driver.find_element_by_name("senha")
        elem_pass.send_keys("loremsupg")
        elem_pass.send_keys(Keys.RETURN)
        # wait page reloads
        reload_page = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "email"))
        )

    def test_email_field(self):
        driver = self.driver
        driver.get("http://localhost:8080/SmartX/login")
        self.assertIn("Login", driver.title)
        # email
        elem_email = driver.find_element_by_name("email")
        # submmit button
        elem_sub = driver.find_element_by_id("entrar")
        # checks
        elem_email.send_keys("loremsup")
        elem_email.send_keys(Keys.RETURN)
        self.assertIn("disabled", elem_sub.get_attribute('class').split())
        elem_email.clear()
        elem_email.send_keys("")
        self.assertIn("disabled", elem_sub.get_attribute('class').split())

    def test_pass_field(self):
        driver = self.driver
        driver.get("http://localhost:8080/SmartX/login")
        self.assertIn("Login", driver.title)
        # password
        elem_pass = driver.find_element_by_name("senha")
        # submmit button
        elem_sub = driver.find_element_by_id("entrar")
        # checks
        elem_pass.send_keys("loremsup")
        self.assertIn("disabled", elem_sub.get_attribute('class').split())  
        elem_pass.send_keys(Keys.RETURN)
        elem_pass.clear()
        elem_pass.send_keys("")
        self.assertIn("disabled", elem_sub.get_attribute('class').split())  
        elem_pass.send_keys(Keys.RETURN)

    def test_both_fields(self):
        driver = self.driver
        driver.get("http://localhost:8080/SmartX/login")
        self.assertIn("Login", driver.title)
        # password
        elem_pass = driver.find_element_by_name("senha")
        # email
        elem_email = driver.find_element_by_name("email")
        # submmit button
        elem_sub = driver.find_element_by_id("entrar")

        elem_pass.send_keys("")
        elem_email.send_keys("")
        self.assertIn("disabled", elem_sub.get_attribute('class').split())  

    def tearDown(self):
        self.driver.close()
