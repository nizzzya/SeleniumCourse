import pytest
import faker

from pages.product_page import ProductPage

from pages.basket_page import BasketPage

from pages.login_page import LoginPage


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param(
#                                       "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                       marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
class TestsProductPage():
    link = "http://selenium1py.pythonanywhere.com"

    @pytest.mark.skip
    def test_guest_can_add_product_to_basket(self, driver):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(driver, link)
        page.open()
        page.add_product_to_cart()
        page.solve_quiz_and_get_code()
        page.should_be_correct_name_in_success_message()
        page.should_be_correct_price_in_success_message()

    @pytest.mark.skip
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, driver):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(driver, link)
        page.open()
        page.add_product_to_cart()
        page.should_not_be_success_message()

    @pytest.mark.skip
    def test_guest_cant_see_success_message(self, driver):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(driver, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.skip
    def test_message_disappeared_after_adding_product_to_basket(self, driver):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(driver, link)
        page.open()
        page.add_product_to_cart()
        page.should_be_disappeared()

    @pytest.mark.skip
    def test_guest_should_see_login_link_on_product_page(self, driver):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(driver, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.skip
    def test_guest_can_go_to_login_page_from_product_page(self, driver):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(driver, link)
        page.open()
        page.go_to_login_page()

    @pytest.mark.skip
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, driver):
        page = ProductPage(driver, self.link)
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(driver, driver.current_url)
        basket_page.should_not_be_products()
        basket_page.should_be_correct_text_about_ampy_basket()

class TestUserAddToBasketFromProductPage():
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"


    @pytest.fixture(scope="function", autouse=True)
    def setup(self,driver):
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


    def test_user_can_add_product_to_basket(self, driver):
        page = ProductPage(driver, self.link)
        page.open()
        page.add_product_to_cart()
        page.solve_quiz_and_get_code()
        page.should_be_correct_name_in_success_message()
        page.should_be_correct_price_in_success_message()

