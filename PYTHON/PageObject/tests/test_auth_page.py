from pages.auth_page import AuthPage
import time


def test_auth_page(selenium):
    page = AuthPage(selenium)
    time.sleep(3)
    page.enter_email('kuku@tut.by')
    page.enter_pass('123')
    page.btn.click()

    # знак != или == будет зависеть от того вводим ли мы верные значения
    assert page.get_relative_link != '/all_pets', 'login ERROR!'
