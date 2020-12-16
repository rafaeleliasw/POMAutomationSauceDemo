from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class SideBarPage(BasePage):
    # By Locators #
    open_menu = (By.CSS_SELECTOR, ".bm-burger-button > button")
    reset = (By.ID, "reset_sidebar_link")
    logout = (By.ID, "logout_sidebar_link")

    # Page Actions #
    def __init__(self, driver):
        super().__init__(driver)

    def do_logout(self):
        self.press_button(self.open_menu)
        self.do_click(self.reset)
        self.do_click(self.logout)
