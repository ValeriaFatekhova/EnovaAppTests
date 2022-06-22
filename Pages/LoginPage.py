from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    EMAIL = (By.ID, "com.harman.enova.beta:id/emailEditText")
    SERVER = (By.ID, "com.harman.enova.beta:id/selectHostButton")
    PROTOCOL = (By.ID, "com.harman.enova.beta:id/selectProtocolButton")
    SEND_BUTTON = (By.ID, "com.harman.enova.beta:id/submitBtn")
    SERVERS_LIST = (By.ID, "com.harman.enova.beta:id/serverName")
    SKIP_SETTINGS_BUTTON = (By.ID, "com.harman.enova.beta:id/continueButton")
    REGISTRATION_TITLE = (By.ID, "com.harman.enova.beta:id/registrationTitle")
    WARNING_INCORRECT_EMAIL = (By.ID, "com.harman.enova.beta:id/errorText")

    def __init__(self, driver):
        super().__init__(driver)

    def is_login_page(self):
        if self.is_element_by_locator(self.REGISTRATION_TITLE) or self.is_element_by_locator(self.SEND_BUTTON):
            return True
        else:
            return False

    def set_email(self, user_name):
        self.do_send_keys_by_locator(self.EMAIL, user_name)

    def set_server(self, server_name):
        self.do_click_by_locator(self.SERVER)
        elements = self.find_elements(self.SERVERS_LIST)
        for element in elements:
            if self.get_element_text_by_element(element) == server_name:
                self.do_click_by_element(element)
                break

    def click_send_button(self):
        self.do_click_by_locator(self.SEND_BUTTON)

    def is_warning_red_text(self):
        if self.is_element_by_locator(self.WARNING_INCORRECT_EMAIL):
            return True
        else:
            return False

    def skip_settings(self):
        continue_button = self.find_element(self.SKIP_SETTINGS_BUTTON)
        self.do_click_by_element(continue_button)
        continue_button = self.find_element(self.SKIP_SETTINGS_BUTTON)
        self.do_click_by_element(continue_button)

    def login(self, server_name, user_name):
        self.set_email(user_name)
        self.set_server(server_name)
        self.click_send_button()
        self.skip_settings()


