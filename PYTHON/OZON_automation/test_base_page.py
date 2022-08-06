import pytest

from .pages.base_page import BasePage

link = "https://ozon.ru/"


@pytest.mark.title
class TestTitleFromBasePage:
    def test_guest_can_change_currency(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_change_currency()

    def test_guest_can_change_area(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_change_area()

    def test_guest_can_change_delivery_address(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_change_delivery_address()

    def test_guest_can_go_to_mobile_app_link(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_go_to_mobile_app_link()

    def test_guest_can_go_to_seller_ozon_link(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_go_to_seller_ozon_link()

    def test_guest_can_go_to_referral_program_link(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_go_to_referral_program_link()

    def test_guest_can_go_to_certificates_link(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_go_to_certificates_link()

    def test_guest_can_go_to_help_link(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_go_to_help_link()

    def test_guest_can_go_to_points_of_issue_link(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_go_to_points_of_issue_link()

    def test_guest_can_go_to_ozon_icon(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_go_to_ozon_icon()

    def test_guest_can_click_on_the_catalogue_button(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_click_on_the_catalogue_button()

    def test_guest_can_go_to_everywhere_dropdown(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_go_to_everywhere_dropdown()

    def test_guest_can_insert_a_phrase_in_the_input_area(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_insert_a_phrase_in_the_input_area()

    def test_guest_can_use_the_search_button(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_insert_a_phrase_in_the_input_area()
        page.guest_can_use_the_search_button()

    def test_guest_can_go_to_login_icon(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_go_to_login_icon()

    def test_guest_can_go_to_orders_icon(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_go_to_orders_icon()

    def test_guest_can_go_to_favorites_icon(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_go_to_favorites_icon()

    def test_guest_can_go_to_basket_icon(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_go_to_basket_icon()

    def test_guest_can_go_to_top_fashion_link(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_go_to_top_fashion_link()

    def test_guest_can_go_to_actions_link(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_go_to_actions_link()

    def test_guest_can_go_to_brands_link(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_go_to_brands_link()

    def test_guest_can_go_to_electronic_link(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_go_to_electronic_link()

    def test_guest_can_go_to_technic_link(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_go_to_technic_link()

    def test_guest_can_go_to_clothes_and_shoes_link(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_go_to_clothes_and_shoes_link()

    def test_guest_can_go_to_beauty_and_health_link(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_go_to_beauty_and_health_link()

    def test_guest_can_go_to_sport_and_relax_link(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_go_to_sport_and_relax_link()

    def test_guest_can_go_to_house_and_garden_link(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_go_to_house_and_garden_link()

    def test_guest_can_go_to_kids_toys_link(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_go_to_kids_toys_link()


class TestBodyBannersBasePage:
    def test_guest_can_see_ozon_banner(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_see_ozon_banner()

    def test_guest_can_see_input_area(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_see_input_area()

    def test_guest_can_see_enter_button(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_see_enter_button()

    def test_guest_can_see_all_actions_link(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_see_all_actions_link()

    def test_guest_can_see_login_button(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_see_login_button()

    def test_guest_can_see_school_things_banner(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_see_school_things_banner()

    def test_guest_can_see_school_and_sport_banner(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_see_school_and_sport_banner()

    def test_guest_can_see_backpacks_banner(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_see_backpacks_banner()

    def test_guest_can_see_sales_banner(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_see_sales_banner()

    def test_guest_can_see_mega_sales_banner(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_see_mega_sales_banner()

    def test_guest_can_see_super_sales_banner(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_see_super_sales_banner()

    def test_guest_can_see_save_vitamins_banner(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_see_save_vitamins_banner()


class TestFooterBasePage:
    def test_guest_can_go_to_your_goods_link(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_go_to_your_goods_link()

    def test_guest_can_go_to_sell_on_ozon_link(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_go_to_sell_on_ozon_link()

    def test_guest_can_go_to_referral_footer_link(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.guest_can_go_to_referral_footer_link()
