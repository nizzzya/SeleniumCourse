import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="You must choose language")


@pytest.fixture(scope="function")
def driver(request):
    choose_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': choose_language})
    driver = webdriver.Chrome(options=options)
    yield driver
    # time.sleep(9)
    driver.close()
    driver.quit()
