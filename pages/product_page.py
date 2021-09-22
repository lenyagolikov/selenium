from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def press_button_add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button.click()

    @staticmethod
    def should_be_correct_product_name_after_adding(product_name, product_name_in_basket):
        assert product_name == product_name_in_basket, 'Incorrect product name in basket'

    @staticmethod
    def should_be_correct_product_price_after_adding(product_price, product_price_in_basket):
        assert product_price == product_price_in_basket, 'Incorrect product price in basket'

    def get_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), 'Product name is not present'
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name

    def get_product_name_in_message(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_NAME_IN_MESSAGE), 'Product name in basket is not present'
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        return product_name

    def get_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), 'Product price is not present'
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price

    def get_product_price_in_message(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE), 'Product price in basket is not present'
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE).text
        return product_price
