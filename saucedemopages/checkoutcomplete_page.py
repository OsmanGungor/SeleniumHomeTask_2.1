from selenium.webdriver.common.by import By
from saucedemopages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    def __init__(self, driver):
        super().__init__('checkout-complete.html', driver)
        self.thanks_text_locator = (By.CLASS_NAME, 'complete-header')

    def get_thanks_text(self):
        thanks_text = self.driver.find_element(*self.thanks_text_locator).text
        return thanks_text
