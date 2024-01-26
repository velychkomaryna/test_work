from .page import Page

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

class LoginPage(Page):
    
    def __init__(self, driver):
        super().__init__(driver)

    def find_element(self, xpath):
        return self.driver.find_element(MobileBy.XPATH, xpath)

    def click_element(self, element):
        return element.click()
    
    def wait_for_element(self, element_xpath, timeout=10):

        try:
            WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((MobileBy.XPATH, element_xpath))
        )
        except TimeoutException:
            logging.info("Stay on the login page")
            raise TimeoutException
        logging.info("Login successful. Go to next page")

    def input_text(self, element, text):
        return element.send_keys(text)

    def clear_input(self, element):
        return element.clear()
    
    def get_page(self):
        return self.driver.get_page_source