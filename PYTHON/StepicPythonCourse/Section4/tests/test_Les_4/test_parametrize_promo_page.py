import pytest
from .pages.promo_page import PromoPage

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

url = [f"{product_base_link}?promo=offer{no}" if no != "???"
       else pytest.param("bugged_link", marks=pytest.mark.xfail) for no in range(10)]


@pytest.mark.parametrize('link', url)
def test_guest_can_add_product_to_basket(browser, link):
    page = PromoPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.button_add_click()
    page.solve_quiz_and_get_code()
    page.checking_goods_price_and_basket_price_are_the_same()
    page.checking_name_ordered_book_and_book_in_basket()
