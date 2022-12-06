import time

from selenium.webdriver.common.by import By


class TestOskarSite:

    def test_exist_button_add_to_cart(self, driver):
        driver.get(driver.current_url + "catalogue/coders-at-work_207")
        time.sleep(30)

        assert driver.find_element(By.XPATH, "//*[@id=\"add_to_basket_form\"]/button")
