import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num_1 = browser.find_element(By.ID, "num1").text
    num_2 = browser.find_element(By.ID, "num2").text
    x = int(num_1)
    y = int(num_2)
    Summary = str(x + y)
    dropdown = browser.find_element(By.ID, "dropdown").click()
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select_number = select.select_by_value(Summary)
    click_btn = browser.find_element(By.XPATH, "//form/button").click()
    time.sleep(5)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
