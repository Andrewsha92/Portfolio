import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    input_firstname = browser.find_element(By.CSS_SELECTOR, "[name = 'firstname']")
    input_lastname = browser.find_element(By.CSS_SELECTOR, "[name = 'lastname']")
    input_email = browser.find_element(By.CSS_SELECTOR, "[name = 'email']")

    input_firstname.send_keys("OK")
    input_lastname.send_keys("OK")
    input_email.send_keys("OK")

    fileInput = browser.find_element(By.CSS_SELECTOR, "#file")
    fileInput.send_keys('C:/Users/Andrew Shabailov/PycharmProjects/StepicPythonCourse/Section2/file.txt')


    submit_btn = browser.find_element(By.XPATH, "//form/button").click()
    time.sleep(5)

finally:
    browser.quit()
