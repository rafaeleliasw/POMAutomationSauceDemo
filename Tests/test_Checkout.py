from Config.config import TestData
from Pages.CheckoutPage import CheckoutPage
from Pages.HeaderPage import HeaderPage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.SideBarPage import SideBarPage
from Tests.test_base import BaseTest


class TestCheckout(BaseTest):

    def test_checkout(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.STANDARD_USER_NAME, TestData.PASSWORD)
        self.homePage = HomePage(self.driver)
        assert self.homePage.get_products_title() == "Products"
        self.homePage.add_backpack_tocart()
        self.homePage.add_light_tocart()
        self.homePage.add_tshirt_tocart()
        self.header = HeaderPage(self.driver)
        assert self.header.get_cart_items() == "3"
        self.header.go_to_cart()
        self.checkout = CheckoutPage(self.driver)
        self.checkout.press_checkout()
        self.checkout.fill_information("Rafael", "Elias", "10001")
        assert "55.97" in self.checkout.get_subtotal()
        assert "4.48" in self.checkout.get_taxes()
        assert "60.45" in self.checkout.get_total()
        self.checkout.press_finish()
        assert self.checkout.get_complete_message() == "THANK YOU FOR YOUR ORDER"
        self.sidebar = SideBarPage(self.driver)
        self.sidebar.do_logout()

    def test_continueshoppingandcheckout(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        self.checkout = CheckoutPage(self.driver)
        self.header = HeaderPage(self.driver)
        self.loginPage.do_login(TestData.STANDARD_USER_NAME, TestData.PASSWORD)
        assert self.homePage.get_products_title() == "Products"
        self.homePage.add_backpack_tocart()
        self.header.go_to_cart()
        self.checkout.press_continueshopping()
        self.homePage.add_light_tocart()
        self.homePage.add_tshirt_tocart()
        assert self.header.get_cart_items() == "3"
        self.header.go_to_cart()
        self.checkout.press_checkout()
        self.checkout.fill_information("Rafael", "Elias", "10001")
        assert "55.97" in self.checkout.get_subtotal()
        assert "4.48" in self.checkout.get_taxes()
        assert "60.45" in self.checkout.get_total()
        self.checkout.press_finish()
        assert self.checkout.get_complete_message() == "THANK YOU FOR YOUR ORDER"
        self.sidebar = SideBarPage(self.driver)
        self.sidebar.do_logout()

    def test_firstnamerequired(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.STANDARD_USER_NAME, TestData.PASSWORD)
        self.homePage = HomePage(self.driver)
        assert self.homePage.get_products_title() == "Products"
        self.homePage.add_backpack_tocart()
        self.homePage.add_light_tocart()
        self.homePage.add_tshirt_tocart()
        self.header = HeaderPage(self.driver)
        assert self.header.get_cart_items() == "3"
        self.header.go_to_cart()
        self.checkout = CheckoutPage(self.driver)
        self.checkout.press_checkout()
        self.checkout.fill_information("", "Elias", "10001")
        assert self.checkout.get_error_message() == "Error: First Name is required"
        self.sidebar = SideBarPage(self.driver)
        self.sidebar.do_logout()

    def test_lastnamerequired(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.STANDARD_USER_NAME, TestData.PASSWORD)
        self.homePage = HomePage(self.driver)
        assert self.homePage.get_products_title() == "Products"
        self.homePage.add_backpack_tocart()
        self.homePage.add_light_tocart()
        self.homePage.add_tshirt_tocart()
        self.header = HeaderPage(self.driver)
        assert self.header.get_cart_items() == "3"
        self.header.go_to_cart()
        self.checkout = CheckoutPage(self.driver)
        self.checkout.press_checkout()
        self.checkout.fill_information("Rafael", "", "10001")
        assert self.checkout.get_error_message() == "Error: Last Name is required"
        self.sidebar = SideBarPage(self.driver)
        self.sidebar.do_logout()

    def test_zipcoderequired(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        self.checkout = CheckoutPage(self.driver)
        self.header = HeaderPage(self.driver)
        self.loginPage.do_login(TestData.STANDARD_USER_NAME, TestData.PASSWORD)
        assert self.homePage.get_products_title() == "Products"
        self.homePage.add_backpack_tocart()
        self.homePage.add_light_tocart()
        self.homePage.add_tshirt_tocart()
        assert self.header.get_cart_items() == "3"
        self.header.go_to_cart()
        self.checkout.press_checkout()
        self.checkout.fill_information("Rafael", "Elias", "")
        assert self.checkout.get_error_message() == "Error: Postal Code is required"
        self.sidebar = SideBarPage(self.driver)
        self.sidebar.do_logout()

    def test_removefromcheckout(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        self.checkout = CheckoutPage(self.driver)
        self.header = HeaderPage(self.driver)
        self.loginPage.do_login(TestData.STANDARD_USER_NAME, TestData.PASSWORD)
        assert self.homePage.get_products_title() == "Products"
        self.homePage.add_backpack_tocart()
        self.homePage.add_light_tocart()
        assert self.header.get_cart_items() == "2"
        self.header.go_to_cart()
        self.checkout.remove_backpack_fromcart()
        assert self.header.get_cart_items() == "1"
        self.sidebar = SideBarPage(self.driver)
        self.sidebar.do_logout()
