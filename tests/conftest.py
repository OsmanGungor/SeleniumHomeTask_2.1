import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from saucedemopages.pagefactory import PageFactory


@pytest.fixture(scope="function")
def create_page_factory():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    page_factory = PageFactory(driver)
    yield page_factory
    driver.quit()


@pytest.fixture(scope="function")
def login_user(create_page_factory):
    page_factory = create_page_factory
    index_page = page_factory.get_page_instance('index_page')
    index_page.open_page()
    index_page.populate_username_textbox('standard_user')
    index_page.populate_password_textbox('secret_sauce')
    index_page.click_login()
    yield page_factory
