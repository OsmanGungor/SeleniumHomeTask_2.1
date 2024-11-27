from utils.logging_config import configure_logging, get_logger

configure_logging()


class BasePage:
    def __init__(self, url, page):
        self.page = page
        self.baseurl = 'https://www.saucedemo.com/'
        self.url = self.baseurl + url
        self.logger = get_logger()

    def open_page(self):
        try:
            self.page.goto(self.url)
            self.logger.info("navigate_to_url", action="page navigation", url=self.url)
        except Exception as e:
            self.logger.error("navigation_error", url=self.url, error=str(e))
            raise
