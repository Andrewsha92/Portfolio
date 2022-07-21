import time

from selenium import webdriver

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.execute_script("document.title='Script executing';alert('Robots at work');")
    time.sleep(5)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
