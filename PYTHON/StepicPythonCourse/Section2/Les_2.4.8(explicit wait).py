import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


try:
    driver = webdriver.Chrome()

    driver.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = driver.find_element(By.ID, "book").click()


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = driver.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    input_answer = driver.find_element(By.CSS_SELECTOR, '#answer')
    input_answer.send_keys(y)
    down_button = driver.find_element(By.ID, "solve").click()

    alert = driver.switch_to.alert
    alert_text = alert.text
    print(alert_text)


finally:
    # закрываем браузер после всех манипуляций
    driver.quit()
