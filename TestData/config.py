import time


class TestData:
    APPLICATION = r"C:\Users\ruvkuminov\eNova_Beta_1.1.4.175.apk"
    DEVICE = "emulator-5554"  # "VFFDU19B08002278"

    DESIRED_CAPABILITIES = {'app': APPLICATION,
                            'appPackage': 'com.harman.enova.beta',
                            'appActivity': 'com.harman.enova.MainActivity',
                            'platformName': 'Android', 'deviceName': DEVICE,
                            'autoGrantPermissions': True,
                            'adbExecTimeout': 500000,
                            'newCommandTimeout': 500000
                            }

    LOGIN_DATA = {"SERVER": "US West", "USER_NAME": "tbd@gmail.com", "PROTOCOL": "Websocket", "LANGUAGE": "English"}
    SETTINGS_DATA = {"pauseDetectionTimeoutLayout": "5000"}
    CUSTOMER = "Enova"

    AUDIO_FOR_SINGLE_INTENTS = [
        ("../TestData/AudioData/what time is it.mp3", "What time is it", ""),

    ]

    AUDIO_FOR_DIALOGS = []

    # PASSWORD = "TBD"
    # REPORT_TEMPLATE_PATH = '../report_template.xlsx'
    # REPORT_PATH = f'../reports/report_{time.strftime("%Y_%m_%d_%H_%M_%S")}.xlsx'

