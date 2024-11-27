import pytest


@pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce"),
                                               ("problem_user", "secret_sauce"),
                                               ("error_user", "secret_sauce"),
                                               ("visual_user", "secret_sauce")])
def test_successful_login(create_page_factory, username, password):
    page_factory = create_page_factory
    page_index = page_factory.get_page_instance('index_page')
    page_index.open_page()
    page_index.populate_username_textbox(username)
    page_index.populate_password_textbox(password)
    page_index.click_login()
    inventory_page = page_factory.get_page_instance('inventory_page')
    current_url = inventory_page.url
    assert current_url == inventory_page.url, f"Wrong URL, URL did not change as expected. Current URL: {current_url}"


@pytest.mark.parametrize("username,password,expected_text",
                         [("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
                          ("wrong_user", "wrong_password",
                           "Epic sadface: Username and password do not match any user in this service")])
def test_unsuccessful_login(create_page_factory, username, password, expected_text):
    page_factory = create_page_factory
    page_index = page_factory.get_page_instance('index_page')
    page_index.open_page()
    page_index.populate_username_textbox(username)
    page_index.populate_password_textbox(password)
    page_index.click_login()
    current_text = page_index.get_error_message_text()
    assert expected_text == current_text, f"Wrong text. Current Text: {current_text}"


@pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce"),
                                               ("performance_glitch_user", "secret_sauce")])
def test_slow_login(create_page_factory, username, password):
    page_factory = create_page_factory
    page_index = page_factory.get_page_instance('index_page')
    page_index.open_page()
    page_index.populate_username_textbox(username)
    page_index.populate_password_textbox(password)
    logging_duration = page_index.click_login_and_measure_time()
    max_duration = 3
    assert logging_duration <= max_duration, f"Login took too long: {logging_duration} seconds"
