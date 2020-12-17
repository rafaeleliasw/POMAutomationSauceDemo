from Config.config import TestData
from Pages.HeaderPage import HeaderPage
from Pages.HomePage import HomePage
from Pages.InventoryItemPage import InventoryItemPage
from Pages.LoginPage import LoginPage
from Pages.SideBarPage import SideBarPage
from Tests.test_base import BaseTest


class TestHomePage(BaseTest):

    def test_add_remove_items(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.STANDARD_USER_NAME, TestData.PASSWORD)
        self.homePage = HomePage(self.driver)
        self.homePage.open_inventory_item4()
        self.inventoryitemPage = InventoryItemPage(self.driver)
        self.inventoryitemPage.add_to_cart()
        self.header = HeaderPage(self.driver)
        assert self.header.get_cart_items() == "1"
        self.inventoryitemPage.remove_from_cart()
        self.inventoryitemPage.press_back()
        assert self.homePage.get_products_title() == "Products"
        self.sidebar = SideBarPage(self.driver)
        self.sidebar.do_logout()