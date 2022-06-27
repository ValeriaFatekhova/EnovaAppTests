import pytest
from appium import webdriver
from Pages.LoginPage import LoginPage
from TestData.config import TestData


@pytest.fixture(scope='function')
def driver(request):
    test_data = TestData()

    driver = webdriver.Remote("http://localhost:4723/wd/hub", test_data.DESIRED_CAPABILITIES)
    print(driver)
    request.cls.driver = driver

    yield
    driver.close_app()
    driver.quit()


@pytest.fixture(scope='function', params=[("US West", "tbd@gmail.com", "Websocket", "English")])
def login(driver, request):
    server = request.param[0]
    user = request.param[1]
    protocol = request.param[2]
    language = request.param[3]

    login_page = LoginPage(request.cls.driver)

    login_page.login(server, user, protocol, language)


