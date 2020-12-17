from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class HomePage(BasePage):
    # By Locators #
    products_title = (By.XPATH, "//*[@id='inventory_filter_container']/div")
    add_backpack_btn = (By.CSS_SELECTOR, ".inventory_item:nth-child(1) .btn_primary")
    add_light_btn = (By.CSS_SELECTOR, ".inventory_item:nth-child(2) .btn_primary")
    add_tshirt_btn = (By.CSS_SELECTOR, ".inventory_item:nth-child(3) .btn_primary")
    remove_backpack_btn = (By.XPATH, "//div[3]/button")
    remove_light_btn = (By.XPATH, "//div[2]/div[3]/button")
    inventory_item4 = (By.CSS_SELECTOR, "#item_4_img_link > .inventory_item_img")

    # Page Actions #
    def __init__(self, driver):
        super().__init__(driver)

    def get_products_title(self):
        pr_title = self.get_element_text(self.products_title)
        return pr_title

    def add_backpack_tocart(self):
        self.press_button(self.add_backpack_btn)

    def remove_backpack_fromcart(self):
        self.press_button(self.remove_backpack_btn)

    def add_light_tocart(self):
        self.press_button(self.add_light_btn)

    def remove_light_fromcart(self):
        self.press_button(self.remove_light_btn)

    def add_tshirt_tocart(self):
        self.press_button(self.add_tshirt_btn)

    def open_inventory_item4(self):
        self.press_button(self.inventory_item4)
