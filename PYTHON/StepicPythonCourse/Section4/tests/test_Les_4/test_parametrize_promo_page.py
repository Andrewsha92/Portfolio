import pytest
from .pages.promo_page import PromoPage


@pytest.mark.parametrize('promo_offer',
                         [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason='Failed test')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = PromoPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.button_add_click()
    page.solve_quiz_and_get_code()
    page.checking_goods_price_and_basket_price_are_the_same()
    page.checking_name_ordered_book_and_book_in_basket()
