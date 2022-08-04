from .pages.newnegative_page import NewPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = NewPage(browser, link)
    page.open()
    page.button_add_click()
    page.should_not_be_success_message_is_not_present()


def test_guest_cant_see_success_message(browser):
    page = NewPage(browser, link)
    page.should_not_be_success_message_is_not_present()


def test_message_disappeared_after_adding_product_to_basket(browser):
    page = NewPage(browser, link)
    page.open()
    page.button_add_click()
    page.should_not_be_success_message_is_disappeared()
