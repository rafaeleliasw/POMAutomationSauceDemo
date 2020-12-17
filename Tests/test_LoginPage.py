from Config.config import TestData
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.SideBarPage import SideBarPage
from Tests.test_base import BaseTest


class TestLogin(BaseTest):

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.STANDARD_USER_NAME, TestData.PASSWORD)
        self.homePage = HomePage(self.driver)
        assert self.homePage.get_products_title() == "Products"
        self.sidebar = SideBarPage(self.driver)
        self.sidebar.do_logout()

    def test_logininvalidpassword(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.STANDARD_USER_NAME, "InvalidPassword")
        assert self.loginPage.get_error_message() == "Epic sadface: Username and password do not match any user in this service"

    def test_loginlockeduser(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.LOCKED_USER_NAME, TestData.PASSWORD)
        assert self.loginPage.get_error_message() == "Epic sadface: Sorry, this user has been locked out."

    def test_loginwithnousername(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login("", TestData.PASSWORD)
        assert self.loginPage.get_error_message() == "Epic sadface: Username is required"

    def test_loginwithnopassword(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.STANDARD_USER_NAME, "")
        assert self.loginPage.get_error_message() == "Epic sadface: Password is required"
