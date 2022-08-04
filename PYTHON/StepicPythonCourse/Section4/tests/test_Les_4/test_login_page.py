from .pages.login_page import LoginPage

link = "https://selenium1py.pythonanywhere.com/accounts/login/"


def test_sub_login_in_url(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()


def test_login_form_on_the_page(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()


def test_register_form_on_the_page(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()
