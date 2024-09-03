import time
from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants import TIMEOUT
from utils.logging_config import configure_logging, get_logger

configure_logging()


class BasePage:
    def __init__(self, url, driver):
        self.driver = driver
        self.baseurl = 'https://www.saucedemo.com/'
        self.url = self.baseurl + url
        self.logger = get_logger()

    def open_page(self):
        self.logger.info("Opening page", url=self.url)
        self.driver.get(self.url)
        self.wait_page_url()
        self.wait_page_ready()

    def wait_page_url(self):
        wait = WebDriverWait(self.driver, TIMEOUT)
        self.logger.info("Waiting for page URL")
        wait.until(lambda driver: self.url in driver.current_url, f"Page url is expected to be {self.url}")
        self.logger.info("Page URL is as expected")
        return self.driver.current_url

    def wait_page_ready(self):
        wait = WebDriverWait(self.driver, TIMEOUT)
        self.logger.info("Waiting for page to be ready")
        wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete",
                   f"Page is not in readyState 'complete'")
        self.logger.info("Page is ready")
        time.sleep(1)

    def wait_element_displayed(self, locator):
        wait = WebDriverWait(self.driver, TIMEOUT)
        wait.until(EC.visibility_of_element_located(locator), f"Element is not displayed: {locator}")

    def js_scroll(self, locator, retries=3, delay=2):
        for attempt in range(retries):
            try:
                element = self.driver.find_element(*locator)
                self.driver.execute_script("arguments[0].scrollIntoView();", element)
                time.sleep(1)
                return element
            except (StaleElementReferenceException, NoSuchElementException) as e:
                if attempt == retries - 1:
                    raise type(e)(f"Unable to scroll on the element '{locator}' after {retries} attempts: {str(e)}")
                time.sleep(delay)

    def js_scroll_and_js_click(self, locator, retries=3, delay=2):
        self.wait_element_displayed(locator)
        for attempt in range(retries):
            try:
                element = self.js_scroll(locator)
                self.driver.execute_script("arguments[0].click();", element)
                return element
            except (StaleElementReferenceException, NoSuchElementException) as e:
                if attempt == retries - 1:
                    raise type(e)(f"Unable to click on the element '{locator}' after {retries} attempts: {str(e)}")
                time.sleep(delay)

    def js_scroll_and_js_click_element(self, element, retries=3, delay=2):
        for attempt in range(retries):
            try:
                self.driver.execute_script("arguments[0].scrollIntoView();", element)
                self.driver.execute_script("arguments[0].click();", element)
                return element
            except (StaleElementReferenceException, NoSuchElementException) as e:
                if attempt == retries - 1:
                    raise type(e)(f"Unable to click on the element '{element}' after {retries} attempts: {str(e)}")
                time.sleep(delay)

    def send_keys(self, locator, value):
        self.wait_element_displayed(locator)
        self.driver.find_element(*locator).send_keys(value)
        self.logger.info(f"Element with {locator}, has been populated with the value:{value}")
