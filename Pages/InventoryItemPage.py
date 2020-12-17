from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class InventoryItemPage(BasePage):
    # By Locators #
    add_btn = (By.CSS_SELECTOR, ".btn_primary")
    remove_btn = (By.CSS_SELECTOR, ".btn_secondary")
    back_btn = (By.CSS_SELECTOR, ".inventory_details_back_button")

    # Page Actions #
    def __init__(self, driver):
        super().__init__(driver)

    def add_to_cart(self):
        self.press_button(self.add_btn)

    def remove_from_cart(self):
        self.press_button(self.remove_btn)

    def press_back(self):
        self.press_button(self.back_btn)

