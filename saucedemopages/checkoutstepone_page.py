from saucedemopages.base_page import BasePage
from constants import TEST_CUSTOMER


class CheckoutStepOnePage(BasePage):
    def __init__(self, page):
        super().__init__('checkout-step-one.html', page)
        self.firstname_box_locator = '#first-name'
        self.lastname_box_locator = '#last-name'
        self.postalcode_box_locator = '#postal-code'
        self.continue_button_locator = '#continue'

    def fill_firstname(self):
        self.page.fill(self.firstname_box_locator, TEST_CUSTOMER.name)
        self.logger.info("Firstname textbox filled")


    def fill_lastname(self):
        self.page.fill(self.lastname_box_locator, TEST_CUSTOMER.lastname)
        self.logger.info("Surname textbox filled")


    def fill_postalcode(self):
        self.page.fill(self.postalcode_box_locator, TEST_CUSTOMER.postalcode)
        self.logger.info("Postalcode textbox filled")


    def click_continue(self):
        self.page.locator(self.continue_button_locator).click()
        self.logger.info("Continue button clicked.")


    def populate_checkout_information(self):
        self.fill_firstname()
        self.fill_lastname()
        self.fill_postalcode()
        self.click_continue()
