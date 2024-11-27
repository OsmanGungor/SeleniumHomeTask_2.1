from saucedemopages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    def __init__(self, page):
        super().__init__('checkout-complete.html', page)
        self.thanks_text_locator = '.complete-header'

    def get_thanks_text(self):
        thanks_text = self.page.locator(self.thanks_text_locator).text_content()
        self.logger.info("Thanking text got")
        return thanks_text
