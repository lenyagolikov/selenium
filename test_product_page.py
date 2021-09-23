import pytest

from pages.product_page import ProductPage


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


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    page.should_not_disappeared()
