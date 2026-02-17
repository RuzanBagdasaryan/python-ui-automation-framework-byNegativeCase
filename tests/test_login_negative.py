from Page.login_page import LoginPage

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("wrong_user", "wrong_pass")

    error_message = login_page.get_error_message()
    assert "Username and password do not match" in error_message

def test_empty_fields(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("", "")

    error_message = login_page.get_error_message()
    assert "Username is required" in error_message

