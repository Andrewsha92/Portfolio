from .base_page import BasePage
from .locators import ProductPageLocators


class PromoPage(BasePage):

    def button_add_click(self):
        button_add = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button_add.click()

    def checking_name_ordered_book_and_book_in_basket(self):
        ordered_book = self.browser.find_element(*ProductPageLocators.ORDERED_BOOK).text
        name_of_book_in_basket = self.browser.find_element(*ProductPageLocators.THE_BOOK_IN_BASKET).text
        print(ordered_book, name_of_book_in_basket)
        assert ordered_book == name_of_book_in_basket, \
            'The name of book on during order and the name of book in basket are not the same'

    def checking_goods_price_and_basket_price_are_the_same(self):
        price_of_book = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK).text
        price_of_basket = self.browser.find_element(*ProductPageLocators.PRICE_OF_BASKET).text
        print(price_of_book, price_of_basket)
        assert price_of_book == price_of_basket, 'The price of book and the price of basket are not the same'
