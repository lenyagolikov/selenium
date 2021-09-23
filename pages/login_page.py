from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert LoginPageLocators.LOGIN_URL in self.browser.current_url, 'URL is not valid'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not presented'

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_INPUT_EMAIL)
        input_email.send_keys(email)
        input_password1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_INPUT_PASSWORD1)
        input_password1.send_keys(password)
        input_password2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_INPUT_PASSWORD2)
        input_password2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON_SUBMIT)
        button.click()
