from selenium.webdriver.common.by import By
from saucedemopages.base_page import BasePage
from constants import TEST_CUSTOMER


class CheckoutStepOnePage(BasePage):
    def __init__(self, driver):
        super().__init__('checkout-step-one.html', driver)
        self.firstname_box_locator = (By.ID, 'first-name')
        self.lastname_box_locator = (By.ID, 'last-name')
        self.postalcode_box_locator = (By.ID, 'postal-code')
        self.continue_button_locator = (By.ID, 'continue')

    def fill_firstname(self):
        super().send_keys(self.firstname_box_locator, TEST_CUSTOMER.name)

    def fill_lastname(self):
        super().send_keys(self.lastname_box_locator, TEST_CUSTOMER.lastname)

    def fill_postalcode(self):
        super().send_keys(self.postalcode_box_locator, TEST_CUSTOMER.postalcode)

    def click_continue(self):
        super().js_scroll_and_js_click(self.continue_button_locator)

    def populate_checkout_information(self):
        self.fill_firstname()
        self.fill_lastname()
        self.fill_postalcode()
        self.click_continue()
