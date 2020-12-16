from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class HeaderPage(BasePage):
    # By Locators #
    cart_items = (By.CSS_SELECTOR, ".fa-layers-counter")

    # Page Actions #
    def __init__(self, driver):
        super().__init__(driver)

    def get_cart_items(self):
        items = self.get_element_text(self.cart_items)
        return items

    def go_to_cart(self):
        self.do_click(self.cart_items)