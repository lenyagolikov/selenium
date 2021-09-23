from .base_page import BasePage
from .locators import CartPageLocators

from selenium.common.exceptions import NoSuchElementException


class CartPage(BasePage):
    def should_be_empty_cart(self):
        try:
            self.browser.find_element(*CartPageLocators.TEXT_CART_IS_EMPTY)
        except NoSuchElementException:
            assert False, 'Cart should be empty'

    def should_not_be_empty_cart(self):
        try:
            self.browser.find_element(*CartPageLocators.TEXT_CART_IS_EMPTY)
        except NoSuchElementException:
            pass
        else:
            assert False, 'Cart should be not empty'

    def should_be_text_is_empty_cart(self):
        text = self.browser.find_element(*CartPageLocators.TEXT_CART_IS_EMPTY).text
        assert len(text) > 0, 'Text for empty cart should be'

    def should_not_be_text_is_empty_cart(self):
        text = self.browser.find_element(*CartPageLocators.TEXT_CART_IS_EMPTY).text
        assert len(text) == 0, 'Text for empty cart is not should be'
