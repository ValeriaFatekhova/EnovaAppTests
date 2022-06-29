from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class EnovaChatPage(BasePage):
    SKIP_TUTORIAL_BUTTON = (By.ID, "com.harman.enova.beta:id/skipButton")
    MIC_BUTTON = (By.ID, "com.harman.enova.beta:id/recordBtn")
    LISTENING_STATE_BUTTON = (By.ID, "com.harman.enova.beta:id/listeningView")
    SERVER_PROCESSING_BUTTON = (By.ID, "com.harman.enova.beta:id/processingView")
    CHAT_BACK_BUTTON = (By.ID, "com.harman.enova.beta:id/closeBtn")
    CHAT_TEXT = (By.ID, "com.harman.enova.beta:id/requestTextView")
    METRICS = (By.ID, "com.harman.enova.beta:id/metricsLayout")
    METRICS_TEXT = (By.ID, "com.harman.enova.beta:id/metricsTextView")

    def __init__(self, driver):
        super().__init__(driver)

    def skip_tutorial(self):
        self.click_by_locator(self.SKIP_TUTORIAL_BUTTON)

    def listening_mode_on(self):
        if self.is_element_by_locator(self.SKIP_TUTORIAL_BUTTON):
            self.skip_tutorial()
        if self.is_listening_mode_off():
            self.click_by_locator(self.MIC_BUTTON)

    def is_listening_mode_on(self):
        if self.is_element_by_locator(self.LISTENING_STATE_BUTTON):
            return True
        else:
            return False

    def is_listening_mode_off(self):
        if self.is_element_by_locator(self.MIC_BUTTON):
            return True
        else:
            return False

    def is_server_processing_state(self):
        if self.is_element_by_locator(self.SERVER_PROCESSING_BUTTON):
            return True
        else:
            return False

    def is_metrics_in_chat(self):
        if self.is_element_by_locator(self.METRICS):
            return True
        else:
            return False

    def get_metrics_text(self):
        if self.is_metrics_in_chat():
            return self.get_element_text_by_locator(self.METRICS_TEXT)
        else:
            return None

    def is_data_in_metrix(self):
        metrics_text = self.get_metrics_text().split(",")
        metrix = dict()
        for m in metrics_text:
            temp = [m.split("=")]
            metrix[temp[0][0]] = temp[0][1]
        if None not in metrix.values() and "" not in metrix.values():
            return True
        else:
            return False

    def exit_from_chatmode(self):
        self.click_by_locator(self.CHAT_BACK_BUTTON)

    # def play_audio_in_chat(self, audio):
    #     if self.is_listening_mode_on():
    #         self.a.play(audio)
    #     while not self.is_listening_mode_off():
    #         self.pause(10)
    #     return self.get_element_text_by_locator(self.CHAT_TEXT)

    def send_question_in_chat_not_dialog(self, audio_path):
        self.listening_mode_on()
        self.play(audio_path)
        self.is_listening_mode_off()

    def get_answer_from_chat(self):
        pass

    def check_answer_in_chat(self):
        pass
