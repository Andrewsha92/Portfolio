import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestParametrizeTime:
    @pytest.fixture(scope="function")
    def browser(self):
        print("\nstart browser for test..")
        browser = webdriver.Chrome()

        yield browser
        print("\nquit browser..")
        browser.quit()

    @pytest.mark.parametrize('link_number',
                             ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
    def test_get_parametrize_link(self, browser, link_number):
        link = f"https://stepik.org/lesson/{link_number}/step/1"
        browser.get(link)
        browser.implicitly_wait(7)
        text_area = browser.find_element(By.TAG_NAME, 'textarea')
        answer = math.log(int(time.time()))
        text_area.send_keys(answer)
        submit = browser.find_element(By.CLASS_NAME, 'submit-submission').click()
        text = browser.find_element(By.TAG_NAME, "p")
        message = text.text
        if message != "Correct":
            print(message)
        assert message == 'Correct!', "The text message is not 'Correct!'"


















