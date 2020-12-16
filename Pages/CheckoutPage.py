from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class CheckoutPage(BasePage):
    # By Locators #
    checkout_button = (By.LINK_TEXT, "CHECKOUT")
    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    zip_code = (By.ID, "postal-code")
    continue_button = (By.XPATH, "//input[@value='CONTINUE']")
    continueshopping_button = (By.XPATH, "//a[contains(text(), 'Continue Shopping')]")
    finish_button = (By.LINK_TEXT, "FINISH")
    subtotal = (By.CSS_SELECTOR, ".summary_subtotal_label")
    taxes = (By.CSS_SELECTOR, ".summary_tax_label")
    total = (By.CSS_SELECTOR, ".summary_total_label")
    complete_message = (By.CSS_SELECTOR, ".complete-header")
    error_message = (By.CSS_SELECTOR, "[data-test='error']")
    remove_backpack_btn = (By.CSS_SELECTOR, ".cart_item:nth-child(3) .btn_secondary")

    # Page Actions #
    def __init__(self, driver):
        super().__init__(driver)

    def press_checkout(self):
        self.press_button(self.checkout_button)

    def press_continueshopping(self):
        self.press_button(self.continueshopping_button)

    def fill_information(self, firstname, lastname, zipcode):
        self.send_keys(self.first_name, firstname)
        self.send_keys(self.last_name, lastname)
        self.send_keys(self.zip_code, zipcode)
        self.press_button(self.continue_button)

    def press_finish(self):
        self.press_button(self.finish_button)

    def get_subtotal(self):
        subtotal = self.get_element_text(self.subtotal)
        return subtotal

    def get_taxes(self):
        tax = self.get_element_text(self.taxes)
        return tax

    def get_total(self):
        total = self.get_element_text(self.total)
        return total

    def get_complete_message(self):
        message = self.get_element_text(self.complete_message)
        return message

    def get_error_message(self):
        error = self.get_element_text(self.error_message)
        return error

    def remove_backpack_fromcart(self):
        self.press_button(self.remove_backpack_btn)
