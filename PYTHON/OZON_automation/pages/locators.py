from selenium.webdriver.common.by import By


class BasePageHeaderLocators:
    LOGIN_ICON = (By.CSS_SELECTOR, "#stickyHeader > div.q7c div > div > span.wc")
    CHANGE_CURRENCY = (By.CSS_SELECTOR, "div > div.uc7.ui-b0")
    CHANGE_AREA = (By.CSS_SELECTOR, "div.k.k0.l1")
    CHANGE_DELIVERY_ADDRESS = (
        By.CSS_SELECTOR, "div.l3 > div> div > div > div:nth-child(3) > div > button > span > span")
    MOBILE_APP_LINK = (By.CSS_SELECTOR, "li:nth-child(1) > div > a > span")
    SELLER_OZON_LINK = (By.CSS_SELECTOR, "li:nth-child(2) > div > a > span")
    REFERRAL_PROGRAM_LINK = (By.CSS_SELECTOR, "li:nth-child(3) > div > a > span")
    CERTIFICATES_LINK = (By.CSS_SELECTOR, "li:nth-child(4) > div > a > span")
    HELP_LINK = (By.CSS_SELECTOR, "li:nth-child(5) > div > a > span")
    POINTS_OF_ISSUE_LINK = (
        By.CSS_SELECTOR, "#layoutPage > div.b4 > div.g1d > div > ul > li:nth-child(7) > div > a > span")
    OZON_ICON = (By.CSS_SELECTOR, "#stickyHeader > div.w0c > a > img")
    CATALOGUE_BUTTON = (By.CSS_SELECTOR, " div.q7c > div > div.ui-b0 > button > span")
    EVERYWHERE_DROPDOWN = (By.CSS_SELECTOR, "span.aia")
    INPUT_AREA = (By.CSS_SELECTOR, "input:nth-child(1)")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button > svg")
    ORDERS_ICON = (By.CSS_SELECTOR, "#stickyHeader > div.c8q > div.ui-l7.u3f > a")
    FAVORITES_ICON = (By.CSS_SELECTOR, "a:nth-child(3) > span.wc")
    BASKET_ICON = (By.CSS_SELECTOR, "a:nth-child(4) > span.wc")
    TOP_FASHION_LINK = (By.CSS_SELECTOR, "li:nth-child(1) > a")
    ACTIONS_LINK = (By.CSS_SELECTOR, "li:nth-child(2) > a")
    BRANDS_LINK = (By.CSS_SELECTOR, "li:nth-child(3) > a")
    ELECTRONIC_LINK = (By.CSS_SELECTOR, "li:nth-child(4) > a")
    TECHNIC_LINK = (By.CSS_SELECTOR, "li:nth-child(5) > a")
    CLOTHES_AND_SHOES_LINK = (By.CSS_SELECTOR, "li:nth-child(6) > a")
    BEAUTY_AND_HEALTH_LINK = (By.CSS_SELECTOR, "li:nth-child(7) > a")
    SPORT_AND_RELAX_LINK = (By.CSS_SELECTOR, "li:nth-child(8) > a")
    HOUSE_AND_GARDEN_LINK = (By.CSS_SELECTOR, "li:nth-child(9) > a")
    KIDS_TOYS_LINK = (By.CSS_SELECTOR, "li:nth-child(10) > a")


class BasePageBodyLocators:
    OZON_BANNER = (By.CSS_SELECTOR, "div.container.b8 > div:nth-child(1) > a > img")
    SCROLL_BANNER = (By.CSS_SELECTOR, "div:nth-child(1) > div > a > div > img")
    INPUT_AREA = (By.CSS_SELECTOR, "div> div > input")
    ENTER_BUTTON = (By.CSS_SELECTOR, "div:nth-child(2) > div.oc7 > div > div > button")
    ALL_ACTIONS_LINK = (By.CSS_SELECTOR, "div.o7c > a")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "div.co7 > div > div > button > span > span")
    SCHOOL_THINGS_BANNER = (By.CSS_SELECTOR, "div:nth-child(7) > a > img")
    SCHOOL_AND_SPORT_BANNER = (By.CSS_SELECTOR, "div:nth-child(9) > div > a:nth-child(1) > img")
    BACKPACKS_BANNER = (By.CSS_SELECTOR, "div:nth-child(9) > div > a:nth-child(2) > img")
    SALES_BANNER = (By.CSS_SELECTOR, "div:nth-child(9) > div > a:nth-child(3) > img")
    MEGA_SALES_BANNER = (By.CSS_SELECTOR, "div:nth-child(10) > div > a:nth-child(1) > img")
    SUPER_SALES_BANNER = (By.CSS_SELECTOR, "div:nth-child(10) > div > a:nth-child(2) > img")
    SAVE_VITAMINS_BANNER = (By.CSS_SELECTOR, "div:nth-child(10) > div > a:nth-child(3) > img")
    HOT_BUY_BUTTON = (By.CSS_SELECTOR, "div.wb9a.ui-c5 > button > span > span")
    IN_BASKET_BUTTON = (By.CSS_SELECTOR, "div:nth-child(1) > div:nth-child(1) > div.bwa9 > div.b9aw > div:nth-child(1)"
                                         " > div.dx2 > div.d8x > div > div > button > span > span")
    PET_SALES_BANNER = (By.CSS_SELECTOR, "div:nth-child(1) > div.bv7a > div > a:nth-child(1) > img")
    KIDS_SALES_BANNER = (By.CSS_SELECTOR, "div:nth-child(1) > div.bv7a > div > a:nth-child(2) > img")
    PREMIUM_HOUSE_BANNER = (By.CSS_SELECTOR, "div:nth-child(1) > div.bv7a > div > a:nth-child(3) > img")
    YOKE_SUN_BANNER = (By.CSS_SELECTOR, "div:nth-child(1) > div.bv7a > div > a:nth-child(4) > img")


class BasePageFooterLocators:
    YOUR_GOODS_LINK = (By.CSS_SELECTOR, "div.cp7 div > div:nth-child(1) > a:nth-child(2)")
    SELL_ON_OZON_LINK = (By.CSS_SELECTOR, "div.cp7 div > div:nth-child(1) > a:nth-child(3)")
    REFERRAL_PROGRAM_LINK = (By.CSS_SELECTOR, "div.cp7 div > div:nth-child(1) > a:nth-child(4)")
    SET_OZON_BOX_LINK = (By.CSS_SELECTOR, "div.pc7 > div > div:nth-child(1) > a:nth-child(5)")
    OPEN_ON_OZON_POINT_LINK = (By.CSS_SELECTOR, "div.cp7 div > div:nth-child(1) > a:nth-child(6)")
    BECOME_DELIVER_LINK = (By.CSS_SELECTOR, "div.cp7 div > div:nth-child(1) > a:nth-child(7)")
    WHAT_SELL_LINK = (By.CSS_SELECTOR, "div.cp7 div > div:nth-child(1) > a:nth-child(8)")
    SELLING_ON_OZON_LINK = (By.CSS_SELECTOR, "div.cp7 div > div:nth-child(1) > a:nth-child(9)")
    ABOUT_OZON_LINK = (By.CSS_SELECTOR, "div.cp7 div > div:nth-child(2) > a:nth-child(2)")
    BECOME_COURIER_LINK = (By.CSS_SELECTOR, "div.cp7 div > div:nth-child(2) > a:nth-child(3)")
    PRESS_CONTACTS_LINK = (By.CSS_SELECTOR, "div.cp7 div > div:nth-child(2) > a:nth-child(4)")
    REQUISITES_LINK = (By.CSS_SELECTOR, "div.cp7 div > div:nth-child(2) > a:nth-child(5)")
    OZON_BALLON_LINK = (By.CSS_SELECTOR, "div.cp7 div > div:nth-child(2) > a:nth-child(6)")
    OZON_BRAND_LINK = (By.CSS_SELECTOR, "div.cp7 div > div:nth-child(2) > a:nth-child(7)")
    HOT_LINE_LINK = (By.CSS_SELECTOR, "div.cp7 div > div:nth-child(2) > a:nth-child(8)")
    STABLE_DEVELOPMENT_LINK = (By.CSS_SELECTOR, "div.cp7 div > div:nth-child(2) > a:nth-child(9)")
    OZON_CARE_LINK = (By.CSS_SELECTOR, "div.cp7 div > div:nth-child(2) > a:nth-child(10)")
    PERSONAL_DATA_LINK = (By.CSS_SELECTOR, "div.cp7 div > div:nth-child(2) > a:nth-child(11)")
    HOW_ORDER_LINK = (By.CSS_SELECTOR, "div.cp7 div > div:nth-child(3) > a:nth-child(2)")
    DELIVERY_LINK = (By.CSS_SELECTOR, "div.cp7 div > div:nth-child(3) > a:nth-child(3)")
    PAYMENT_LINK = (By.CSS_SELECTOR, "div.cp7 div > div:nth-child(3) > a:nth-child(4)")
    CONTACTS_LINK = (By.CSS_SELECTOR, "div.cp7 div > div:nth-child(3) > a:nth-child(5)")
    SAFETY_LINK = (By.CSS_SELECTOR, "div.pc7 > div > div:nth-child(3) > a:nth-child(6)")
    ALL_RIGHTS_LINK = (By.CSS_SELECTOR, "div.c5p > div:nth-child(1) > a")
    VK_LINK = (By.CSS_SELECTOR, "div.c5x > a:nth-child(1) > svg")
    OK_LINK = (By.CSS_SELECTOR, "div.c5x > a:nth-child(2) > svg")
    TG_LINK = (By.CSS_SELECTOR, "div.c5x > a:nth-child(3) > svg")
    BETTER_VISION = (By.CSS_SELECTOR, "div.pc8 > div > button > span > span")
    STOP_COVID_LINK = (By.CSS_SELECTOR, "div > div.pc7 > a > img")
    OZON_LINK = (By.CSS_SELECTOR, "div.p8c > div:nth-child(1) > a")
    OZON_VACANCIES_LINK = (By.CSS_SELECTOR, "div.c8p > div:nth-child(2) > a")
    ROUTE_256_LINK = (By.CSS_SELECTOR, "div.c8p > div:nth-child(3) > a")
    LITRES_RU_LINK = (By.CSS_SELECTOR, "div.c8p > div:nth-child(4) > a")


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, "div.pn5 button > span > span")
    GOODS_VALUE_IN_HEADER = (By.CSS_SELECTOR, "a:nth-child(4) span.tsCaptionBold.v9c")
    IN_BASKET_BUTTON = (By.CSS_SELECTOR, "a:nth-child(4) span.tsCaptionBold.v9c")
    BASKET = (By.CSS_SELECTOR, "div.q7c > a:nth-child(4)")
    GODS_VALUE_IN_BASKET = (By.CSS_SELECTOR, "div:nth-child(3) div.ra6")
    ORDER_PRICE = (By.CSS_SELECTOR, "div.xk8.x9k span.x8k")
    BASKET_PRICE = (By.CSS_SELECTOR, "div:nth-child(6) div span span")
    POP_UP = (By.CSS_SELECTOR, "div.m2c button > span svg")


class ParametrizePageLocators:
    SEARCH_STRING = (By.CSS_SELECTOR, "div.ai2a > input:nth-child(1)")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#stickyHeader > div.qc9 > div > form > button")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div:nth-child(2) > div.aia > div:nth-child(2) > div.aa0i")
