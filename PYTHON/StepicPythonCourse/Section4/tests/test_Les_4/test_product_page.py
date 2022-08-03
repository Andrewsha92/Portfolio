from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.button_add_click()  # кликаем на кнопку добавить
    page.solve_quiz_and_get_code()
    page.guest_can_add_product_to_basket()  # выполняем метод страницы — переходим на страницу логина


def test_checking_goods_price_and_basket_price_are_the_same(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.button_add_click()  # кликаем на кнопку добавить
    page.solve_quiz_and_get_code()
    page.checking_goods_price_and_basket_price_are_the_same()


def test_checking_name_ordered_book_and_book_in_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.button_add_click()  # кликаем на кнопку добавить
    page.solve_quiz_and_get_code()
    page.checking_name_ordered_book_and_book_in_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.click_on_basket()
    page.the_basket_is_empty()
    page.price_of_basket_is_not_present()
