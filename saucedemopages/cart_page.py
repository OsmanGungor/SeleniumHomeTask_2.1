from saucedemopages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__('cart', page)
        self.inventory_item_locator = '.inventory_item_name'
        self.check_out_button_locator = '#checkout'

    def get_added_product_titles(self):
        elements_list = self.page.query_selector_all(self.inventory_item_locator)
        title_list = []
        for element in elements_list:
            title_list.append(element.text_content())
        self.logger.info("Got added product titles")
        return title_list


    def click_checkout(self):
        self.page.locator(self.check_out_button_locator).click()
        self.logger.info("Checkout button clicked")

