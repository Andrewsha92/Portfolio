from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert 'login' in login_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email: str, password: str):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "Email field is not present"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), "Password field is not present"
        assert self.is_element_present(*LoginPageLocators.CONFIRM_PASSWORD), "Confirm password field is not present"
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "Register button is not present"

        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
