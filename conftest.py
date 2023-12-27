import pytest
from selenium import webdriver
import requests
from data.urls import ENDPOINTS, URLS
from helpers import ProfileMethods
from pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1280,1024')
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        options_firefox = webdriver.FirefoxOptions()
        options_firefox.add_argument('--window-size=1280,1024')
        driver = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield driver
    driver.quit()


@pytest.fixture
def create_new_user_with_delete():
    user_data = ProfileMethods.generate_user()
    response = requests.post(URLS.MAIN_PAGE + ENDPOINTS.CREATE_USER, user_data)
    yield user_data, response
    headers = {'Authorization': response.json()['accessToken']}
    requests.delete(URLS.MAIN_PAGE + ENDPOINTS.DELETE_USER, headers=headers)


@pytest.fixture
def login_user(driver, create_new_user_with_delete):
    user_data = create_new_user_with_delete[0]
    login_page = LoginPage(driver, URLS.MAIN_PAGE + URLS.LOGIN_PAGE)
    login_page.open_page()
    login_page.login(user_data['email'], user_data['password'])
