from selenium.webdriver.common.by import By
from saucedemopages.base_page import BasePage
from utils.common_utilities import extract_and_convert_to_decimal


class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__('inventory.html', driver)
        self.inventory_item_locator = (By.CLASS_NAME, 'inventory_item')
        self.product_title_locator = (By.CLASS_NAME, 'inventory_item_name')
        self.product_price_locator = (By.CLASS_NAME, 'inventory_item_price')
        self.add_to_chart_button_locator = (By.CSS_SELECTOR, "button[id*='add-to-cart']")
        self.cart_symbol_locator = (By.CLASS_NAME, "shopping_cart_link")

    def add_to_cart(self, item_title):
        total_price = 0
        item_dictionary = {}
        list_of_all_product_elements = self.driver.find_elements(*self.inventory_item_locator)
        for product in list_of_all_product_elements:
            title_text = product.find_element(*self.product_title_locator).text
            item_dictionary[title_text] = product
        for title in item_title:
            product = item_dictionary.get(title)
            if product is not None:
                add_to_cart_button_element = product.find_element(*self.add_to_chart_button_locator)
                super().js_scroll_and_js_click_element(add_to_cart_button_element)
                rawprice = product.find_element(*self.product_price_locator).text
                decimal_price = extract_and_convert_to_decimal(rawprice)
                total_price += decimal_price
            else:
                f'Product with title:{title} does not exist'
        return total_price

    def click_cart_symbol(self):
        cart_symbol_element = self.driver.find_element(*self.cart_symbol_locator)
        super().js_scroll_and_js_click_element(cart_symbol_element)
