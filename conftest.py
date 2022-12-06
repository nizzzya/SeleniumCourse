from datetime import time

import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='uk',
                     help="You must choose language")


@pytest.fixture(scope="function")
def driver(request):

    url_site = "https://selenium1py.pythonanywhere.com/"
    choose_language = request.config.getoption("language")

    driver = webdriver.Chrome()
    driver.get(url_site+choose_language)
    driver.implicitly_wait(2)

    yield driver
    driver.close()
    driver.quit()

