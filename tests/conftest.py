import pytest
from playwright.sync_api import sync_playwright
from saucedemopages.pagefactory import PageFactory


@pytest.fixture(scope="function")
def create_page_factory():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    _page = context.new_page()
    yield PageFactory(_page)
    _page.close()
    context.close()
    browser.close()
    playwright.stop()


@pytest.fixture(scope="function")
def login_user(create_page_factory):
    page_factory = create_page_factory
    index_page = page_factory.get_page_instance('index_page')
    index_page.open_page()
    index_page.populate_username_textbox('standard_user')
    index_page.populate_password_textbox('secret_sauce')
    index_page.click_login()
    yield page_factory
