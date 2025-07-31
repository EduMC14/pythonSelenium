import pytest

from pages.login_page import LoginPage

@pytest.mark.usefixtures("driver")

def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in login_page.get_message()

def  test_login_wrong_username(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.login("wronguser", "SuperSecretPassword!")
    assert "Your username is invalid!" in login_page.get_message()

def test_login_wrong_password(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.login("tomsmith", "wrongpassword")
    assert "Your password is invalid!" in login_page.get_message()
