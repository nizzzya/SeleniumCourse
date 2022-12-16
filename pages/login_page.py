from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.driver.find_element(*LoginPageLocators.EMAIL_FOR_REGISTRATION).send_keys(email)
        self.driver.find_element(*LoginPageLocators.PASSWORD_FOR_REGISTRATION).send_keys(password)
        self.driver.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FOR_REGISTRATION).send_keys(password)
        self.driver.find_element(*LoginPageLocators.BUTTON_REGISTRATION).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.driver.current_url
        assert url.find("login") != -1

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "There is no Log In form on the page"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "There is no Registration form on the page"



