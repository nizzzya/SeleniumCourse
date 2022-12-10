import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestLoginPage():
    base_link = "http://selenium1py.pythonanywhere.com/"
    login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

    def test_ulr_login_page(self, driver):
        mainPage = MainPage(driver, self.base_link)
        mainPage.open()
        mainPage.go_to_login_page()
        page = LoginPage(driver, "")
        page.should_be_login_url()

    def test_exist_login_form(self, driver):
        page = LoginPage(driver, self.login_link)
        page.open()
        page.should_be_login_form()

    def test_exist_registration_form(self, driver):
        page = LoginPage(driver, self.login_link)
        page.open()
        page.should_be_register_form()