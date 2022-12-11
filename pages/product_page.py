from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.alert import Alert


class ProductPage(BasePage):

    def add_product_to_cart(self):
        self.driver.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def should_be_correct_name_in_success_message(self):
        product_name = self.driver.find_element(*ProductPageLocators.NAME_BOOK).text
        product_name_in_success_msg = self.driver.find_element(*ProductPageLocators.SUCCESS_BLOCK_NAME_BOOK).text
        assert product_name == product_name_in_success_msg, "Name of the book is differs"

    def should_be_correct_price_in_success_message(self):
        price_name = self.driver.find_element(*ProductPageLocators.PRICE_OF_THE_BOOK).text
        price_name_in_success_msg = self.driver.find_element(*ProductPageLocators.SUCCESS_BLOCK_PRICE).text
        assert price_name == price_name_in_success_msg, "Book's price is differs"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

