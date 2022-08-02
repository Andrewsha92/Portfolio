from .pages.explicit_wait_page import ExplicitPage


def test_explicit_wait_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ExplicitPage(browser,
                        link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.button_add_click()  # кликаем на кнопку добавить
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message_is_not_pres()
    page.should_not_be_success_message_is_not_disappeared()
