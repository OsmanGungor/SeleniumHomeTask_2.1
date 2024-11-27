import time
from saucedemopages.base_page import BasePage
from playwright.sync_api import expect


class IndexPage(BasePage):
    def __init__(self, page):
        super().__init__('', page)
        self.login_logo_locator = ".login_logo"
        self.index_logo_locator = '.app_logo'
        self.username_textbox_locator = '#user-name'
        self.password_textbox_locator = '#password'
        self.login_button_locator = '#login-button'
        self.error_message_locator = "xpath = //h3[@data-test='error']"

    def open_page(self):
        super().open_page()
        expect(self.page.locator(self.login_logo_locator)).to_be_visible()

    def populate_username_textbox(self, username):
        self.page.locator(self.username_textbox_locator).fill(username)
        self.logger.info("Username textbox filled")


    def populate_password_textbox(self, password):
        self.page.locator(self.password_textbox_locator).fill(password)
        self.logger.info("Password textbox filled")

    def click_login(self):
        self.page.locator(self.login_button_locator).click()
        self.logger.info("Login button clicked")

    def get_error_message_text(self):
        error_message_text = self.page.locator(self.error_message_locator).text_content()
        self.logger.info("Text of the message has ben taken.")
        return error_message_text

    def click_login_and_measure_time(self):
        start_time = time.time()
        self.page.locator(self.login_button_locator).click()
        self.logger.info("Login button clicked")
        self.page.locator(self.index_logo_locator).wait_for(state="visible")
        end_time = time.time()
        logging_duration = end_time - start_time
        self.logger.info(f"Login duration measured: {logging_duration:.2f} seconds")
        return logging_duration
