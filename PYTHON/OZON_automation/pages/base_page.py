from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageTitleLocators, BasePageBodyLocators, BasePageFooterLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def guest_can_change_currency(self):
        self.browser.find_element(*BasePageTitleLocators.CHANGE_CURRENCY)
        assert self.is_element_present(*BasePageTitleLocators.CHANGE_CURRENCY), "Icon with currency is not presented"

    def guest_can_change_area(self):
        self.browser.find_element(*BasePageTitleLocators.CHANGE_CURRENCY)
        assert self.is_element_present(*BasePageTitleLocators.CHANGE_AREA), "Icon with area is not presented"

    def guest_can_change_delivery_address(self):
        self.browser.find_element(*BasePageTitleLocators.CHANGE_DELIVERY_ADDRESS)
        assert self.is_element_present(
            *BasePageTitleLocators.CHANGE_DELIVERY_ADDRESS), "Icon with delivery address is not presented"

    def guest_can_go_to_mobile_app_link(self):
        self.browser.find_element(*BasePageTitleLocators.MOBILE_APP_LINK)
        assert self.is_element_present(
            *BasePageTitleLocators.MOBILE_APP_LINK), "Mobile app link is not presented"

    def guest_can_go_to_seller_ozon_link(self):
        self.browser.find_element(*BasePageTitleLocators.SELLER_OZON_LINK)
        assert self.is_element_present(
            *BasePageTitleLocators.SELLER_OZON_LINK), "Seller referral link is not presented"

    def guest_can_go_to_referral_program_link(self):
        self.browser.find_element(*BasePageTitleLocators.REFERRAL_PROGRAM_LINK)
        assert self.is_element_present(
            *BasePageTitleLocators.REFERRAL_PROGRAM_LINK), "Referral link is not presented"

    def guest_can_go_to_certificates_link(self):
        self.browser.find_element(*BasePageTitleLocators.CERTIFICATES_LINK)
        assert self.is_element_present(
            *BasePageTitleLocators.CERTIFICATES_LINK), "Certificates link is not presented"

    def guest_can_go_to_help_link(self):
        self.browser.find_element(*BasePageTitleLocators.HELP_LINK)
        assert self.is_element_present(
            *BasePageTitleLocators.CERTIFICATES_LINK), "Help link is not presented"

    def guest_can_go_to_points_of_issue_link(self):
        self.browser.find_element(*BasePageTitleLocators.POINTS_OF_ISSUE_LINK)
        assert self.is_element_present(
            *BasePageTitleLocators.CERTIFICATES_LINK), "Points of issue link is not presented"

    def guest_can_go_to_ozon_icon(self):
        self.browser.find_element(*BasePageTitleLocators.OZON_ICON)
        assert self.is_element_present(
            *BasePageTitleLocators.OZON_ICON), "Ozon icon is not presented"

    def guest_can_click_on_the_catalogue_button(self):
        self.browser.find_element(*BasePageTitleLocators.CATALOGUE_BUTTON).click()
        assert self.is_element_present(
            *BasePageTitleLocators.CATALOGUE_BUTTON), "Catalogue button is not presented"

    def guest_can_go_to_everywhere_dropdown(self):
        self.browser.find_element(*BasePageTitleLocators.EVERYWHERE_DROPDOWN)
        assert self.is_element_present(
            *BasePageTitleLocators.EVERYWHERE_DROPDOWN), "Everywhere dropdown is not presented"

    def guest_can_insert_a_phrase_in_the_input_area(self):
        self.browser.find_element(*BasePageTitleLocators.INPUT_AREA).send_keys('justSOMEphrase')
        assert self.is_element_present(
            *BasePageTitleLocators.INPUT_AREA), "Input does not work"

    def guest_can_use_the_search_button(self):
        self.browser.find_element(*BasePageTitleLocators.INPUT_AREA).send_keys('justSOMEphrase')
        assert self.is_element_present(
            *BasePageTitleLocators.SEARCH_BUTTON), "Search button does not work"

    def guest_can_go_to_login_icon(self):
        self.browser.find_element(*BasePageTitleLocators.LOGIN_ICON)
        assert self.is_element_present(
            *BasePageTitleLocators.LOGIN_ICON), "Login icon is not presented"

    def guest_can_go_to_orders_icon(self):
        self.browser.find_element(*BasePageTitleLocators.ORDERS_ICON)
        assert self.is_element_present(
            *BasePageTitleLocators.ORDERS_ICON), "Orders icon is not presented"

    def guest_can_go_to_favorites_icon(self):
        self.browser.find_element(*BasePageTitleLocators.FAVORITES_ICON)
        assert self.is_element_present(
            *BasePageTitleLocators.FAVORITES_ICON), "Favorites icon is not presented"

    def guest_can_go_to_basket_icon(self):
        self.browser.find_element(*BasePageTitleLocators.BASKET_ICON)
        assert self.is_element_present(
            *BasePageTitleLocators.BASKET_ICON), "Basket icon is not presented"

    def guest_can_go_to_top_fashion_link(self):
        self.browser.find_element(*BasePageTitleLocators.TOP_FASHION_LINK)
        assert self.is_element_present(
            *BasePageTitleLocators.TOP_FASHION_LINK), "Top fashion link is not presented"

    def guest_can_go_to_actions_link(self):
        self.browser.find_element(*BasePageTitleLocators.ACTIONS_LINK)
        assert self.is_element_present(
            *BasePageTitleLocators.ACTIONS_LINK), "Actions link is not presented"

    def guest_can_go_to_brands_link(self):
        self.browser.find_element(*BasePageTitleLocators.BRANDS_LINK)
        assert self.is_element_present(
            *BasePageTitleLocators.BRANDS_LINK), "Brands link is not presented"

    def guest_can_go_to_electronic_link(self):
        self.browser.find_element(*BasePageTitleLocators.ELECTRONIC_LINK)
        assert self.is_element_present(
            *BasePageTitleLocators.ELECTRONIC_LINK), "Electronic link is not presented"

    def guest_can_go_to_technic_link(self):
        self.browser.find_element(*BasePageTitleLocators.TECHNIC_LINK)
        assert self.is_element_present(
            *BasePageTitleLocators.TECHNIC_LINK), "Technic link is not presented"

    def guest_can_go_to_clothes_and_shoes_link(self):
        self.browser.find_element(*BasePageTitleLocators.CLOTHES_AND_SHOES_LINK)
        assert self.is_element_present(
            *BasePageTitleLocators.CLOTHES_AND_SHOES_LINK), "Clothes and shoes link is not presented"

    def guest_can_go_to_beauty_and_health_link(self):
        self.browser.find_element(*BasePageTitleLocators.BEAUTY_AND_HEALTH_LINK)
        assert self.is_element_present(
            *BasePageTitleLocators.BEAUTY_AND_HEALTH_LINK), "Beauty and health link is not presented"

    def guest_can_go_to_sport_and_relax_link(self):
        self.browser.find_element(*BasePageTitleLocators.SPORT_AND_RELAX_LINK)
        assert self.is_element_present(
            *BasePageTitleLocators.SPORT_AND_RELAX_LINK), "Sport and relax link is not presented"

    def guest_can_go_to_house_and_garden_link(self):
        self.browser.find_element(*BasePageTitleLocators.HOUSE_AND_GARDEN_LINK)
        assert self.is_element_present(
            *BasePageTitleLocators.HOUSE_AND_GARDEN_LINK), "House and garden link is not presented"

    def guest_can_go_to_kids_toys_link(self):
        self.browser.find_element(*BasePageTitleLocators.KIDS_TOYS_LINK)
        assert self.is_element_present(
            *BasePageTitleLocators.KIDS_TOYS_LINK), "Kids toys link is not presented"

    def guest_can_see_ozon_banner(self):
        self.browser.find_element(*BasePageBodyLocators.OZON_BANNER)
        assert self.is_element_present(
            *BasePageBodyLocators.OZON_BANNER), "Ozon banner is not presented"

    def guest_can_see_input_area(self):
        self.browser.find_element(*BasePageBodyLocators.INPUT_AREA)
        assert self.is_element_present(
            *BasePageBodyLocators.INPUT_AREA), "Input area is not presented"

    def guest_can_see_enter_button(self):
        self.browser.find_element(*BasePageBodyLocators.ENTER_BUTTON)
        assert self.is_element_present(
            *BasePageBodyLocators.ENTER_BUTTON), "Enter button is not presented"

    def guest_can_see_all_actions_link(self):
        self.browser.find_element(*BasePageBodyLocators.ALL_ACTIONS_LINK)
        assert self.is_element_present(
            *BasePageBodyLocators.ALL_ACTIONS_LINK), "All actions link is not presented"

    def guest_can_see_login_button(self):
        self.browser.find_element(*BasePageBodyLocators.LOGIN_BUTTON)
        assert self.is_element_present(
            *BasePageBodyLocators.LOGIN_BUTTON), "Login button is not presented"

    def guest_can_see_school_things_banner(self):
        self.browser.find_element(*BasePageBodyLocators.SCHOOL_THINGS_BANNER)
        assert self.is_element_present(
            *BasePageBodyLocators.SCHOOL_THINGS_BANNER), "School things is not presented"

    def guest_can_see_school_and_sport_banner(self):
        self.browser.find_element(*BasePageBodyLocators.SCHOOL_AND_SPORT_BANNER)
        assert self.is_element_present(
            *BasePageBodyLocators.SCHOOL_AND_SPORT_BANNER), "School and sport is not presented"

    def guest_can_see_backpacks_banner(self):
        self.browser.find_element(*BasePageBodyLocators.BACKPACKS_BANNER)
        assert self.is_element_present(
            *BasePageBodyLocators.BACKPACKS_BANNER), "Backpacks banner is not presented"

    def guest_can_see_sales_banner(self):
        self.browser.find_element(*BasePageBodyLocators.SALES_BANNER)
        assert self.is_element_present(
            *BasePageBodyLocators.SALES_BANNER), "Backpacks banner is not presented"

    def guest_can_see_mega_sales_banner(self):
        self.browser.find_element(*BasePageBodyLocators.MEGA_SALES_BANNER)
        assert self.is_element_present(
            *BasePageBodyLocators.MEGA_SALES_BANNER), "Mega sales banner is not presented"

    def guest_can_see_super_sales_banner(self):
        self.browser.find_element(*BasePageBodyLocators.SUPER_SALES_BANNER)
        assert self.is_element_present(
            *BasePageBodyLocators.SUPER_SALES_BANNER), "Super sales banner is not presented"

    def guest_can_see_save_vitamins_banner(self):
        self.browser.find_element(*BasePageBodyLocators.SAVE_VITAMINS_BANNER)
        assert self.is_element_present(
            *BasePageBodyLocators.SAVE_VITAMINS_BANNER), "Save vitamins banner is not presented"

    def guest_can_go_to_your_goods_link(self):
        self.browser.execute_script("window.scrollBy(0,1000)", "")
        self.browser.find_element(*BasePageFooterLocators.YOUR_GOODS_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.YOUR_GOODS_LINK), "Your goods link is not presented"

    def guest_can_go_to_sell_on_ozon_link(self):
        self.browser.execute_script("window.scrollBy(0,1000)", "")
        self.browser.find_element(*BasePageFooterLocators.SELL_ON_OZON_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.SELL_ON_OZON_LINK), "Sell on Ozon link is not presented"

    def guest_can_go_to_referral_footer_link(self):
        self.browser.execute_script("window.scrollBy(0,1000)", "")
        self.browser.find_element(*BasePageFooterLocators.REFERRAL_PROGRAM_LINK)
        assert self.is_element_present(
            *BasePageFooterLocators.REFERRAL_PROGRAM_LINK), "Referral program link in footer is not presented"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout). \
                until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False
