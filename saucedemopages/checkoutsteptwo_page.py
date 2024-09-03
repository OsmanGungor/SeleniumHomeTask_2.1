from selenium.webdriver.common.by import By
from saucedemopages.base_page import BasePage
from utils.common_utilities import extract_and_convert_to_decimal


class CheckoutStepTwoPage(BasePage):
    def __init__(self, driver):
        super().__init__('checkout-step-two.html', driver)
        self.total_price_locator = (By.CLASS_NAME, 'summary_subtotal_label')
        self.finish_button_locator = (By.ID, 'finish')

    def get_total_price(self):
        raw_price = self.driver.find_element(*self.total_price_locator).text
        decimal_total = extract_and_convert_to_decimal(raw_price)
        return decimal_total

    def click_finish_button(self):
        super().js_scroll_and_js_click(self.finish_button_locator)