from .pages.product_page import ProductPage


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
