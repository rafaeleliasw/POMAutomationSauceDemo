import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Pages.SideBarPage import SideBarPage


@pytest.mark.usefixtures("init_driver")
class BaseTest:

    def __init__(self):
        self.sidebar = SideBarPage(self.driver)
        self.loginPage = LoginPage(self.driver)

    def setup_method(self):
        self.loginPage.do_login(TestData.STANDARD_USER_NAME, TestData.PASSWORD)

    def teardown_method(self):
        self.sidebar.do_logout()
