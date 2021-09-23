from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.browser.find_element(*BasketPageLocators.TEXT_BASKET_IS_EMPTY), 'Basket should be empty'

    def should_not_be_empty_basket(self):
        assert not self.browser.find_element(*BasketPageLocators.TEXT_BASKET_IS_EMPTY), 'Basket should not be empty'

    def should_be_text_is_empty_basket(self):
        text = self.browser.find_element(*BasketPageLocators.TEXT_BASKET_IS_EMPTY).text
        assert len(text) > 0, 'Text for empty cart should be'

    def should_not_be_text_is_empty_basket(self):
        text = self.browser.find_element(*BasketPageLocators.TEXT_BASKET_IS_EMPTY).text
        assert len(text) == 0, 'Text for empty basket should not be'
