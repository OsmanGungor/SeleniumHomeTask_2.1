from selenium.webdriver.common.by import By
from saucedemopages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__('cart', driver)
        self.inventory_item_locator = (By.CLASS_NAME, 'inventory_item_name')
        self.check_out_button_locator = (By.ID, 'checkout')

    def get_added_product_titles(self):
        elements_list = self.driver.find_elements(*self.inventory_item_locator)
        title_list = []
        for element in elements_list:
            title_list.append(element.text)
        return title_list

    def click_checkout(self):
        super().js_scroll_and_js_click(self.check_out_button_locator)
