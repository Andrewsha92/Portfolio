from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_registration_1():
    try:
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        elements = browser.find_elements(By.TAG_NAME, "input")
        for element in elements:
            element.send_keys("Мой ответ")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text, "Something wrong!"

    finally:
        browser.quit()


def test_registration_2():
    try:
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1_FIRST_NAME = browser.find_element(By.XPATH, "//form/div[1]/div[1]/input")
        input1_FIRST_NAME.send_keys("Ivan Shabailov")
        time.sleep(3)

        input2_EMAIL = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.second_class > input")
        input2_EMAIL.send_keys("PASS")

        input3_PHONE = browser.find_element(By.XPATH, "//form/div[2]/div[1]/input")
        input3_PHONE.send_keys("Smolensk")

        input4_ADDRES = browser.find_element(By.XPATH, "//form/div[2]/div[2]/input")
        input4_ADDRES.send_keys("Russia")
        button = browser.find_element(By.XPATH, "//div/form/button")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text, "Something wrong!"

    finally:
        browser.quit()
