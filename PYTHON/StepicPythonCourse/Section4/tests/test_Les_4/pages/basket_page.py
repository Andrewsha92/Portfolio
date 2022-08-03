from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def click_on_basket(self):
        basket = self.browser.find_element(*BasketPageLocators.BASKET)
        basket.click()

    def price_of_basket_is_not_present(self):
        price = self.is_element_present(*BasketPageLocators.PRICE_OF_BASKET)
        assert price == False, "Price is present, basket is not empty"

    def the_basket_is_empty(self):
        empty_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text
        print(empty_text)
        assert f'{empty_text}, No empty message'
