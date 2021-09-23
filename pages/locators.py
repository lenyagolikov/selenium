from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_invalid')
    BUTTON_VIEW_CART = (By.CSS_SELECTOR, '.basket-mini a.btn-default')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class CartPageLocators:
    TEXT_CART_IS_EMPTY = (By.CSS_SELECTOR, '#content_inner p')


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_URL = 'login'
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_INPUT_EMAIL = (By.CSS_SELECTOR, '[name="registration-email"]')
    REGISTRATION_INPUT_PASSWORD1 = (By.CSS_SELECTOR, '[name="registration-password1"]')
    REGISTRATION_INPUT_PASSWORD2 = (By.CSS_SELECTOR, '[name="registration-password2"]')
    REGISTRATION_BUTTON_SUBMIT = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(1) strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(3) strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(1)')
