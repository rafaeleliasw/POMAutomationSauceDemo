from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):

    # By Locators #
    user_name = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_message = (By.CSS_SELECTOR, "[data-test='error']")

    # Page Actions #
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def do_login(self, username, password):
        self.send_keys(self.user_name, username)
        self.send_keys(self.password, password)
        self.press_button(self.login_button)

    def get_error_message(self):
        error = self.get_element_text(self.error_message)
        return error
