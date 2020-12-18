import pytest

from Config.config import TestData


@pytest.mark.usefixtures("init_driver")
class BaseTest:

    def setup_method(self):
        self.loginPage.do_login(TestData.STANDARD_USER_NAME, TestData.PASSWORD)

    def teardown_method(self):
        self.sidebar.do_logout()
