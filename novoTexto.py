import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import lorem

class SmartxNovoTexto(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_new_text(self):
        driver = self.driver
        # do login
        driver.get("http://localhost:8080/SmartX/login")
        self.assertIn("Login", driver.title)
        elem_email = driver.find_element_by_name("email")
        elem_email.send_keys("internet@gmail.com")
        elem_pass = driver.find_element_by_name("senha")
        elem_pass.send_keys("123456")
        elem_pass.send_keys(Keys.RETURN)
        # wait chart_div on index
        index_page = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "chart_div"))
        )

        driver.get("http://localhost:8080/SmartX/producao-textual/novo-texto")
        elem_title = driver.find_element_by_id("titulo")
        # Title
        sentense = lorem.sentence()
        elem_title.send_keys(sentense)
        # Type
        elem_type = Select(driver.find_element_by_id("generoTextual"))
        elem_type.select_by_value("3")
        # Text
        elem_text = driver.find_element_by_id("texto")
        text = lorem.paragraph()
        elem_text.send_keys(text)
        driver.implicitly_wait(20) # seconds
        # Btn
        elem_save_btn = driver.find_element_by_id("btnSalvarTexto")
        elem_save_btn.click()

        loading = WebDriverWait(driver, 30).until(
            EC.invisibility_of_element((By.CLASS_NAME, "con-vs-loading"))
        )

        self.assertIn("Meus textos - SmartX", driver.title)
