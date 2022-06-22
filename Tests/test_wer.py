import pytest
from Tests.test_base import BaseTest
from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Pages.ChooseCustomersScreen import ChooseCustomerScreen
from TestData.config import TestData
from Pages.SettingsInApp import SettingsInApp
from Pages.EnovaChatPage import EnovaChatPage


class TestWer(BaseTest):

    @pytest.mark.parametrize("login_data", [TestData.LOGIN_DATA])
    def test_login(self, login_data):
        self.login_page = LoginPage(self.driver)
        self.settings = SettingsInApp(self.driver)
        self.customers_page = ChooseCustomerScreen(self.driver)
        self.base_page = BasePage(self.driver)

        self.login_page.login(login_data["SERVER"], login_data["USER_NAME"])

        flag = self.base_page.is_element_by_locator(self.customers_page.CUSTOMER_CARD)
        assert flag

        server_name = self.settings.get_server()
        assert server_name == login_data["SERVER"]
