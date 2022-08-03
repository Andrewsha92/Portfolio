from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.click_on_basket()
    page.the_basket_is_empty()
    page.price_of_basket_is_not_present()

