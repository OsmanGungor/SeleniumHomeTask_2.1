from saucedemopages.cart_page import CartPage
from saucedemopages.checkoutcomplete_page import CheckoutCompletePage
from saucedemopages.checkoutstepone_page import CheckoutStepOnePage
from saucedemopages.checkoutsteptwo_page import CheckoutStepTwoPage
from saucedemopages.index_page import IndexPage
from saucedemopages.inventory_page import InventoryPage


class PageFactory:
    def __init__(self, driver):
        self.driver = driver

    def get_page_instance(self, page_name):
        if page_name == 'index_page':
            return IndexPage(self.driver)
        elif page_name == 'inventory_page':
            return InventoryPage(self.driver)
        elif page_name == 'cart_page':
            return CartPage(self.driver)
        elif page_name == 'check_out_step_one_page':
            return CheckoutStepOnePage(self.driver)
        elif page_name == 'check_out_step_two_page':
            return CheckoutStepTwoPage(self.driver)
        elif page_name == 'check_out_step_complete_page':
            return CheckoutCompletePage(self.driver)
        else:
            raise f"Unable to create the instance of: {page_name})"



