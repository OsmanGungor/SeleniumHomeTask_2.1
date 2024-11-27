from saucedemopages.base_page import BasePage
from utils.common_utilities import extract_and_convert_to_decimal


class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__('inventory.html', page)
        self.inventory_item_locator = '.inventory_item'
        self.product_title_locator = '.inventory_item_name'
        self.product_price_locator = '.inventory_item_price'
        self.add_to_chart_button_locator = "button[id*='add-to-cart']"
        self.cart_symbol_locator = ".shopping_cart_link"

    def add_to_cart(self, item_title):
        total_price = 0
        item_dictionary = {}
        list_of_all_product_elements = self.page.query_selector_all(self.inventory_item_locator)
        for product in list_of_all_product_elements:
            title_text = product.query_selector(self.product_title_locator).text_content()
            item_dictionary[title_text] = product
        for title in item_title:
            product = item_dictionary.get(title)
            if product is not None:
                add_to_cart_button_element = product.query_selector(self.add_to_chart_button_locator)
                add_to_cart_button_element.click()
                rawprice = product.query_selector(self.product_price_locator).text_content()
                decimal_price = extract_and_convert_to_decimal(rawprice)
                total_price += decimal_price
            else:
                f'Product with title:{title} does not exist'
        return total_price

    def click_cart_symbol(self):
        self.page.click(self.cart_symbol_locator)
        self.logger.info("Cart Symbol clicked")

