import time
import pytest

from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage


@pytest.mark.parametrize('id', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser, id):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{id}'
    page = ProductPage(browser, link)
    page.open()

    product_name = page.get_product_name()
    product_price = page.get_product_price()

    page.press_button_add_to_basket()

    product_name_in_message = page.get_product_name_in_message()
    product_price_in_message = page.get_product_price_in_message()

    page.should_be_correct_product_name_after_adding(product_name, product_name_in_message)
    page.should_be_correct_product_price_after_adding(product_price, product_price_in_message)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    page.should_not_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_empty_cart()
    cart_page.should_be_text_is_empty_cart()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.user
class TestUserAddToCartFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(str(time.time()) + "@fakemail.org", 'allison1234!')
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()

        product_name = page.get_product_name()
        product_price = page.get_product_price()

        page.press_button_add_to_basket()

        product_name_in_message = page.get_product_name_in_message()
        product_price_in_message = page.get_product_price_in_message()

        page.should_be_correct_product_name_after_adding(product_name, product_name_in_message)
        page.should_be_correct_product_price_after_adding(product_price, product_price_in_message)
