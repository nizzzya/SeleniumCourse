from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_correct_text_about_ampy_basket(self):
        assert self.is_element_present(*BasketPageLocators.MSG_ABOUT_AMPTY_BASKET), "You dont see correct messenger about empty basket"

    def should_not_be_products(self):
        assert self.is_disappeared(*BasketPageLocators.FORM_WITH_PRODUCT), "Your basket isn't empty, but should be"
