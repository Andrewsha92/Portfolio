from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    check_box = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    radio_btn = browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    input_answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_answer.send_keys(y)
   # submit_btn = browser.find_element(By.CSS_SELECTOR,'[type="submit"]').click()
    submit_btn = browser.find_element(By.XPATH,'//div/form/button').click()
    time.sleep(5)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
