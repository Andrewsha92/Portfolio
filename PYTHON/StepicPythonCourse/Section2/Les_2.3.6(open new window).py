import math
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    browser.delete_all_cookies()

    # FIRST_BUTTON = browser.find_element(By.XPATH, "//link[1]").click()
    JS_BUTTON = browser.execute_script("return document.getElementsByTagName('button')[0];")
    browser.execute_script("arguments[0].click();", JS_BUTTON)

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    input_answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_answer.send_keys(y)
    button = browser.find_element(By.XPATH, "//div/button").click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)


finally:
    browser.quit()