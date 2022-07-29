import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()

    yield browser
    print("\nquit browser..")
    browser.quit()


def test_get_parametrize_link(browser):
    link = f"https://stepik.org/lesson/236897/step/1"
    browser.get(link)
    browser.implicitly_wait(7)
    text_area = browser.find_element(By.TAG_NAME, 'textarea')
    answer = math.log(int(time.time()))
    text_area.send_keys(answer)
    submit = browser.find_element(By.CLASS_NAME, 'submit-submission').click()
    Correct = EC.text_to_be_present_in_element((By.TAG_NAME, 'p'), 'Correct!')
    time.sleep(50)