import pytest
from Tests.test_base import BaseTest
from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Pages.ChooseCustomersScreen import ChooseCustomerScreen
from TestData.config import TestData
from Pages.SettingsPage import SettingsInApp
from Pages.EnovaChatPage import EnovaChatPage


class TestEnovaApp(BaseTest):

    """Registering device test"""

    @pytest.mark.parametrize("login_data", [TestData.LOGIN_DATA])
    def test_login(self, login_data):
        self.login_page = LoginPage(self.driver)
        self.settings = SettingsInApp(self.driver)
        self.customers_page = ChooseCustomerScreen(self.driver)
        self.enova_chat = EnovaChatPage(self.driver)

        self.login_page.login(login_data["SERVER"], login_data["USER_NAME"])

        flag = self.customers_page.is_choose_customer_page()
        assert flag

        server_name = self.settings.get_server()
        assert server_name == login_data["SERVER"]

    """Unregistering device test"""

    @pytest.mark.parametrize("login_data", [TestData.LOGIN_DATA])
    def test_logout(self, login_data):
        self.settings = SettingsInApp(self.driver)

        self.settings.unregister_device()

        assert self.login_page.is_login_page()

        self.login_page.click_send_button()
        assert self.login_page.is_warning_red_text()

        self.login_page.login(login_data["SERVER"], login_data["USER_NAME"])

    """Privacy Policy checking test"""

    def test_privacy_policy(self):
        self.settings.open_privacy_policy()

        assert self.settings.is_privacy_policy()

        self.settings.close_privacy_policy()
        self.settings.return_to_customer_screen()

    """Show metrics test"""

    def test_show_metrics(self):
        self.settings.show_metrix_switch_on()
        self.customers_page.open_chatmode_for_customer("Enova")

        assert self.enova_chat.is_metrics_in_chat()
        text_metrix = self.enova_chat.get_metrics_text().split(",")

