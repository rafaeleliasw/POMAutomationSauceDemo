import pytest

from Config.config import TestData
from Pages.HeaderPage import HeaderPage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.SideBarPage import SideBarPage
from Tests.test_base import BaseTest


class TestHomePage(BaseTest):

    def test_addtocart(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.STANDARD_USER_NAME, TestData.PASSWORD)
        self.homePage = HomePage(self.driver)
        assert self.homePage.get_products_title() == "Products"
        self.homePage.add_backpack_tocart()
        self.homePage.add_light_tocart()
        self.homePage.add_tshirt_tocart()
        self.header = HeaderPage(self.driver)
        assert self.header.get_cart_items() == "3"
        self.sidebar = SideBarPage(self.driver)
        self.sidebar.do_logout()

    def test_removefromhomepage(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.STANDARD_USER_NAME, TestData.PASSWORD)
        self.homePage = HomePage(self.driver)
        assert self.homePage.get_products_title() == "Products"
        self.homePage.add_backpack_tocart()
        self.homePage.add_light_tocart()
        self.header = HeaderPage(self.driver)
        assert self.header.get_cart_items() == "2"
        self.homePage.remove_backpack_fromcart()
        assert self.header.get_cart_items() == "1"
        self.sidebar = SideBarPage(self.driver)
        self.sidebar.do_logout()