import allure
import pytest
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from Pages.ChooseCustomersScreen import ChooseCustomerScreen
from TestData.config import TestData
from Pages.SettingsPage import SettingsInApp
from Pages.EnovaChatPage import EnovaChatPage


#@pytest.mark.parametrize("login_data", [TestData.LOGIN_DATA])
class TestEnovaApp(BaseTest):

    """Registering device test"""

    # @pytest.mark.parametrize("login_data", [TestData.LOGIN_DATA])
    # def test_login(self, login_data):
    #     self.login_page = LoginPage(self.driver)
    #     self.settings = SettingsInApp(self.driver)
    #     self.customers_page = ChooseCustomerScreen(self.driver)
    #
    #     self.login_page.login(login_data["SERVER"], login_data["USER_NAME"])
    #
    #     flag = self.customers_page.is_choose_customer_page()
    #     assert flag
    #
    #     server_name = self.settings.get_server()
    #     assert server_name == login_data["SERVER"]

    """Privacy Policy checking test"""

    # def test_privacy_policy(self):
    #     self.settings = SettingsInApp(self.driver)
    #     self.customers_page = ChooseCustomerScreen(self.driver)
    #
    #     self.customers_page.customer_page_is_opened()
    #     self.settings.open_privacy_policy()
    #
    #     assert self.settings.is_privacy_policy()
    #
    #     self.settings.close_privacy_policy()
    #     self.settings.return_to_customer_screen()

    """Show metrics test"""

    @allure.description("Show metrics test")
    def test_show_metrics(self):
        self.settings = SettingsInApp(self.driver)
        self.customers_page = ChooseCustomerScreen(self.driver)
        self.enova_chat = EnovaChatPage(self.driver)

        with allure.step("Switch on 'Show metrics' option in Settings"):
            self.settings.show_metrix_switch_on()
        with allure.step("Open chat for Enova customer"):
            self.customers_page.open_chatmode_for_customer("Enova")
        with allure.step("Make request in chat"):
            self.enova_chat.send_question_in_chat_not_dialog(r"C:\Users\ruvkuminov\TestsAutomation\EnovaAndroidTests\TestData\AudioData\what_time_is_it.mp3")

        with allure.step("Check that metrics are displayed in chat under system answer"):
            assert self.enova_chat.is_metrics_in_chat(), "Metrics is not present in chat after"
        with allure.step("Check that metrics contained not empty data"):
            assert self.enova_chat.is_data_in_metrix(), "Metrics are empty, no data is in metrics"

    """Unregistering device test"""

    @allure.description("Unregistering device test")
    def test_logout(self):
        self.login_page = LoginPage(self.driver)
        self.settings = SettingsInApp(self.driver)
        self.customers_page = ChooseCustomerScreen(self.driver)

        with allure.step("Open Settings -> Device page and click 'Unregister' button"):
            self.settings.unregister_device()

        with allure.step("Check that login page is opened"):
            assert self.login_page.is_login_page()

        with allure.step("Check that 'Email' field is empty and after click 'Submit' button "
                         "messsage about invalid email is displayed"):
            self.login_page.click_send_button()
        assert self.login_page.is_warning_red_text()
