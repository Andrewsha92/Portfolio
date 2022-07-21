import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    check_box = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    input_answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_answer.send_keys(y)

    button = browser.find_element(By.TAG_NAME, "button")
    btn = browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    radio_btn = browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
    button.click()
    time.sleep(5)

finally:
    browser.quit()
