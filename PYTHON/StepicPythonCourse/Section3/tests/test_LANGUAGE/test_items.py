import time

from selenium.webdriver.common.by import By


def test_button_add_with_difference_language_on_page(browser):
    link = browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207')
    time.sleep(30)  # You don't have to use this feature
    assert browser.find_element(By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]'), \
        "The page does not have an 'ADD to basket' button!"

# For starting test you need to use command: pytest -s -v --language=ru test_items.py
# Where param language you choose by yourself
# You can choose: ar, ca, cs, da, de, en-gb, el, es, fi, fr, it, ko. nl, pl, pt, pt-br, ro, ru, sk, uk, zh-hans.
