from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"
options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': 'en'})
browser = webdriver.Chrome(options=options)


def test_language():
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
