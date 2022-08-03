from .base_page import BasePage
from .locators import ProductPageLocators


class NewPage(BasePage):

    def button_add_click(self):
        button_add = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button_add.click()

    def guest_can_add_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), \
            "Button 'add to bag' is not presented"

    def should_not_be_success_message_is_not_pres(self):
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented"

    def should_not_be_success_message_is_disappeared(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented"

    def checking_name_ordered_book_and_book_in_basket(self):
        ordered_book = self.browser.find_element(*ProductPageLocators.ORDERED_BOOK)
        name_of_book_in_basket = self.browser.find_element(*ProductPageLocators.THE_BOOK_IN_BASKET)
        assert ordered_book == name_of_book_in_basket, \
            'The name of book on during oder and the name of book in basket are not the same'

    def checking_goods_price_and_basket_price_are_the_same(self):
        price_of_book = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK)
        price_of_basket = self.browser.find_element(*ProductPageLocators.PRICE_OF_BASKET)
        assert price_of_book == price_of_basket, 'The price of book and the price of basket are not the same'
