from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_be_empty_cart(self):
        assert self.browser.find_element(*CartPageLocators.TEXT_CART_IS_EMPTY), 'Cart should be empty'

    def should_not_be_empty_cart(self):
        assert not self.browser.find_element(*CartPageLocators.TEXT_CART_IS_EMPTY), 'Cart should not be empty'

    def should_be_text_is_empty_cart(self):
        text = self.browser.find_element(*CartPageLocators.TEXT_CART_IS_EMPTY).text
        assert len(text) > 0, 'Text for empty cart should be'

    def should_not_be_text_is_empty_cart(self):
        text = self.browser.find_element(*CartPageLocators.TEXT_CART_IS_EMPTY).text
        assert len(text) == 0, 'Text for empty cart should not be'
