from collections import Counter
import pytest


@pytest.mark.parametrize("item",
                         [["Test.allTheThings() T-Shirt (Red)", "Sauce Labs Onesie"], ["Sauce Labs Bolt T-Shirt"]])
def test_add_to_cart(login_user, item):
    page_factory = login_user
    page_inventory = page_factory.get_page_instance('inventory_page')
    cart_price = page_inventory.add_to_cart(item)
    page_inventory.click_cart_symbol()
    page_cart = page_factory.get_page_instance('cart_page')
    product_titles = page_cart.get_added_product_titles()
    assert Counter(product_titles) == Counter(item), f"Lists do not have the same elements: {item} != {product_titles}"
    page_cart.click_checkout()
    page_checkout_one = page_factory.get_page_instance('check_out_step_one_page')
    page_checkout_one.populate_checkout_information()
    page_checkout_two = page_factory.get_page_instance('check_out_step_two_page')
    decimal_total_price = page_checkout_two.get_total_price()
    assert decimal_total_price == cart_price, f"Prices from cart:{decimal_total_price} is not equal to total{cart_price}"
    page_checkout_two.click_finish_button()
    page_checkout_complete = page_factory.get_page_instance('check_out_step_complete_page')
    thanks_text = page_checkout_complete.get_thanks_text()
    expected_text = 'Thank you for your order!'
    assert thanks_text == expected_text, "Some problem occurred"
