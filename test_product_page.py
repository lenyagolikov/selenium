from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()

    product_name = page.get_product_name()
    product_price = page.get_product_price()

    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()

    product_name_in_message = page.get_product_name_in_message()
    product_price_in_message = page.get_product_price_in_message()

    page.should_be_correct_product_name_after_adding(product_name, product_name_in_message)
    page.should_be_correct_product_price_after_adding(product_price, product_price_in_message)
