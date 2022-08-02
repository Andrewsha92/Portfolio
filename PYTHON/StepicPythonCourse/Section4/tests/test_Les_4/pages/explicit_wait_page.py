from .base_page import BasePage
from .locators import ProductPageLocators


class ExplicitPage(BasePage):

    def button_add_click(self):
        button_add = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button_add.click()

    def should_not_be_success_message_is_not_pres(self):
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented"

    def should_not_be_success_message_is_not_disappeared(self):
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented"
