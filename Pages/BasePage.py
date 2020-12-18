from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

"""This class is the parent of all classes"""
"""It contains all the generic methods and utilities for all pages"""


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).click()

    def press_button(self, by_locator):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(by_locator)).click()

    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return element.text

    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(by_locator))
        return bool(element)

    def is_not_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until_not(ec.presence_of_element_located(by_locator))
        return bool(element)
