from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//span/a[contains(@href, 'basket')]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")
    EMAIL_FOR_REGISTRATION = (By.XPATH, "//input[@name=\"registration-email\"]")
    PASSWORD_FOR_REGISTRATION = (By.XPATH, "//input[@name=\"registration-password1\"]")
    CONFIRM_PASSWORD_FOR_REGISTRATION = (By.XPATH, "//input[@name=\"registration-password2\"]")
    BUTTON_REGISTRATION = (By.XPATH, "//button[@name=\"registration_submit\"]")


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.XPATH, "//*[@id=\"add_to_basket_form\"]/button")
    NAME_BOOK = (By.XPATH, "//h1")
    PRICE_OF_THE_BOOK = (By.XPATH, "//*[@id=\"content_inner\"]//div[@class=\"row\"]//p[@class=\"price_color\"]")
    SUCCESS_BLOCK_NAME_BOOK = (By.XPATH, "//*[@id=\"messages\"]//strong[1]")
    SUCCESS_BLOCK_PRICE = (By.XPATH, "//*[@id=\"messages\"]//p/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id=\"messages\"]//*[@class=\"alertinner\"]")


class BasketPageLocators():
    FORM_WITH_PRODUCT = (By.ID, "basket_formset")
    MSG_ABOUT_AMPTY_BASKET = (By.XPATH, "//*[@id=\"content_inner\"]/p")


