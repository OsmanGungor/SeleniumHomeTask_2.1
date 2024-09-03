import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants import TIMEOUT
from saucedemopages.base_page import BasePage


class IndexPage(BasePage):
    def __init__(self, driver):
        super().__init__('', driver)
        self.login_logo_locator = (By.CLASS_NAME, 'login_logo')
        self.index_logo_locator = (By.CLASS_NAME, 'app_logo')
        self.username_textbox_locator = (By.ID, 'user-name')
        self.password_textbox_locator = (By.ID, 'password')
        self.login_button_locator = (By.ID, 'login-button')
        self.error_message_locator = (By.XPATH, "//h3[@data-test='error']")

    def open_page(self):
        super().open_page()
        assert WebDriverWait(self.driver, TIMEOUT).until(EC.presence_of_element_located(self.login_logo_locator))

    def populate_username_textbox(self, username):
        super().send_keys(self.username_textbox_locator, username)

    def populate_password_textbox(self, password):
        super().send_keys(self.password_textbox_locator, password)

    def click_login(self):
        self.driver.find_element(*self.login_button_locator).click()
        self.logger.info("Login button clicked")

    def get_error_message_text(self):
        error_message = self.driver.find_element(*self.error_message_locator)
        error_massage_text = error_message.text
        self.logger.info("Text of the message has ben taken.")
        return error_massage_text

    def click_login_and_measure_time(self):
        start_time = time.time()
        self.driver.find_element(*self.login_button_locator).click()
        self.logger.info("Login button clicked")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.index_logo_locator))
        end_time = time.time()
        logging_duration = end_time - start_time
        self.logger.info("Login duration got measured.", duration=logging_duration)
        return logging_duration
