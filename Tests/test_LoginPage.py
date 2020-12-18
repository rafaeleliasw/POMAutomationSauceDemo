from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_login_base import BaseLoginTest


class TestLogin(BaseLoginTest):

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.STANDARD_USER_NAME, TestData.PASSWORD)
        assert self.homePage.get_products_title() == "Products"
        self.sidebar.do_logout()

    def test_logininvalidpassword(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.STANDARD_USER_NAME, "InvalidPassword")
        assert self.loginPage.get_error_message() == "Epic sadface: Username and password do not" \
                                                     " match any user in this service"

    def test_loginlockeduser(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.LOCKED_USER_NAME, TestData.PASSWORD)
        assert self.loginPage.get_error_message() == "Epic sadface: Sorry, this user has been locked out."

    def test_loginwithnousername(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.EMPTY_USER_NAME, TestData.PASSWORD)
        assert self.loginPage.get_error_message() == "Epic sadface: Username is required"

    def test_loginwithnopassword(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.STANDARD_USER_NAME, TestData.EMPTY_PASSWORD)
        assert self.loginPage.get_error_message() == "Epic sadface: Password is required"
