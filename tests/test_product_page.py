import pytest
import faker

from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage


class TestsProductPage():
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, driver):
        page = ProductPage(driver, self.link)
        page.open()
        page.add_product_to_cart()
        page.solve_quiz_and_get_code()
        page.should_be_correct_name_in_success_message()
        page.should_be_correct_price_in_success_message()

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, driver):
        page = ProductPage(driver, self.link)
        page.open()
        page.add_product_to_cart()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, driver):
        page = ProductPage(driver, self.link)
        page.open()
        page.should_not_be_success_message()

    def test_message_disappeared_after_adding_product_to_basket(self, driver):
        page = ProductPage(driver, self.link)
        page.open()
        page.add_product_to_cart()
        page.should_be_disappeared()

    def test_guest_should_see_login_link_on_product_page(self, driver):
        page = ProductPage(driver, self.link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, driver):
        page = ProductPage(driver, self.link)
        page.open()
        page.go_to_login_page()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, driver):
        page = ProductPage(driver, self.link)
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(driver, driver.current_url)
        basket_page.should_not_be_products()
        basket_page.should_be_correct_text_about_ampy_basket()


class TestUserAddToBasketFromProductPage():
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"

    # For this test I used package Fake() for generation data for email and password
    # You can install package or create your email and password for registration
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        page = ProductPage(driver, self.link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(driver, driver.current_url)
        f = faker.Faker()
        login_page.register_new_user(f.email(), f.password())
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, driver):
        page = ProductPage(driver, self.link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, driver):
        page = ProductPage(driver, self.link)
        page.open()
        page.add_product_to_cart()
        page.solve_quiz_and_get_code()
        page.should_be_correct_name_in_success_message()
        page.should_be_correct_price_in_success_message()
