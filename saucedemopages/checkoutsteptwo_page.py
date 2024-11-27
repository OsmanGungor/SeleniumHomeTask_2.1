from saucedemopages.base_page import BasePage
from utils.common_utilities import extract_and_convert_to_decimal


class CheckoutStepTwoPage(BasePage):
    def __init__(self, page):
        super().__init__('checkout-step-two.html', page)
        self.total_price_locator = '.summary_subtotal_label'
        self.finish_button_locator = '#finish'

    def get_total_price(self):
        raw_price = self.page.locator(self.total_price_locator).text_content()
        decimal_total = extract_and_convert_to_decimal(raw_price)
        return decimal_total

    def click_finish_button(self):
        self.page.click(self.finish_button_locator)