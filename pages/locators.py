from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.XPATH, "//*[@id=\"add_to_basket_form\"]/button")
    NAME_BOOK = (By.XPATH, "//h1")
    PRICE_OF_THE_BOOK = (By.XPATH, "//*[@id=\"content_inner\"]//div[@class=\"row\"]//p[@class=\"price_color\"]")
    SUCCESS_BLOCK_NAME_BOOK = (By.XPATH, "//*[@id=\"messages\"]//strong[1]")
    SUCCESS_BLOCK_PRICE = (By.XPATH, "//*[@id=\"messages\"]//p/strong")
    SUCCESS_MESSAGE = (By.ID, "messages")

