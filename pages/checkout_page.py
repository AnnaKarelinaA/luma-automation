from selenium.webdriver.common.by import By
from pages.base_page import Page
from features.utils.faker_data import FakeData
import random
from time import sleep


class CheckoutPage(Page, FakeData):
    INPUT_EMAIL = (By.ID, 'customer-email')
    INPUT_FIRST_NAME = (By.NAME, 'firstname')
    INPUT_LAST_NAME = (By.NAME, 'lastname')
    INPUT_STREET_ADDRESS = (By.NAME, 'street[0]')
    INPUT_CITY = (By.NAME, 'city')
    INPUT_ZIP = (By.NAME, 'postcode')
    INPUT_PHONE = (By.NAME, 'telephone')
    DROPDOWN_STATE = (By.NAME, 'region_id')
    DROPDOWN_COUNTRY = (By.NAME, 'country_id')
    SHIPPING_METHODS = (By.CSS_SELECTOR, '.table-checkout-shipping-method .radio')
    BTN_SUBMIT = (By.CSS_SELECTOR, '.button.action.continue')
    PRIMARY_CHECKOUT = (By.CSS_SELECTOR, '.action.primary.checkout')
    ORDER_ID = (By.CSS_SELECTOR, 'p:nth-of-type(1) > span')
    TITLE = (By.CSS_SELECTOR, 'h1')

    def complete_shipping_address(self):

        self.input_text_wait(FakeData().fake_email(), *self.INPUT_EMAIL)
        self.input_text(FakeData().fake_first_name(), *self.INPUT_FIRST_NAME)
        self.input_text(FakeData().fake_first_name(), *self.INPUT_LAST_NAME)
        self.input_text(FakeData().fake_first_name(), *self.INPUT_STREET_ADDRESS)
        self.input_text(FakeData().fake_first_name(), *self.INPUT_CITY)
        self.input_text(FakeData().fake_first_name(), *self.INPUT_ZIP)
        self.input_text(FakeData().fake_first_name(), *self.INPUT_PHONE)
        self.dropdown_select_by_int_value(1, 65, *self.DROPDOWN_STATE)
        self.dropdown_select_by_str_value('US', *self.DROPDOWN_COUNTRY)

    def select_shipping_method(self):
        shipping_options = self.driver.find_elements(*self.SHIPPING_METHODS)
        radio_btn = random.randint(0, 1)
        shipping_options[radio_btn].click()

    def click_proceed_next(self):
        self.click(*self.BTN_SUBMIT)

    def click_order(self):
        sleep(2)  # TODO fix after find solution with jumping button
        self.click_wait(self.PRIMARY_CHECKOUT)

    def verify_order_id(self):
        assert len(self.driver.find_element(*self.ORDER_ID).text) >= 9, \
            f"Expected Order ID not matching actual Order ID {self.driver.find_element(*self.ORDER_ID).text}"

    def verify_key_word_present_url(self, key_word):
        self.verify_url_contains(key_word)

    def verify_success_purchase_text(self, success_text):
        self.verify_two_texts_match(success_text, *self.TITLE)
