from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def open(self):
        self.driver.get(self.url)

    def is_element_present(self, by_how, path):
        try:
            self.driver.find_element(by_how, path)
        except NoSuchElementException:
            return False
        return True
