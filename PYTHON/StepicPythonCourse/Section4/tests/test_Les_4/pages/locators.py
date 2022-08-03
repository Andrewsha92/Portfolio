from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET = (By.XPATH, "//div[2]/span/a")
    PRICE_OF_BASKET = (By.XPATH, "//tr[4]/th[2]/text()")


class BasketPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET = (By.XPATH, "//div[2]/span/a")
    PRICE_OF_BASKET = (By.XPATH, "//tr[12]/td/h3")
    EMPTY_BASKET = (By.XPATH, '//*[@id="content_inner"]/p')



class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR,
                     "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    ORDERED_BOOK = (By.XPATH, "//article/div[1]/div[2]/h1")
    THE_BOOK_IN_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRICE_OF_BOOK = (By.XPATH,
                     "//article/div[1]/div[2]/p[1]")

    PRICE_OF_BASKET = (By.XPATH, "//div[3]/div/p[1]/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div")
