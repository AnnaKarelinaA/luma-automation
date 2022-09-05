from selenium.webdriver.common.by import By
from pages.base_page import Page
from features.utils.faker_data import FakeData


class ContactPage(Page):
    INPUT_NAME = (By.ID, 'name')
    INPUT_EMAIL = (By.ID, 'email')
    INPUT_COMMENT = (By.ID, 'comment')
    BTN_SUBMIT = (By.CSS_SELECTOR, '.action.submit')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.message-success.success.message')
    text = "Thanks for contacting us with your comments and questions." \
           " We'll respond to you very soon."

    def complete_contact_form(self):
        self.input_text(FakeData().fake_name(), *self.INPUT_NAME)
        self.input_text(FakeData().fake_email(), *self.INPUT_EMAIL)
        self.input_text(FakeData().fake_text(), *self.INPUT_COMMENT)

    def submit_contact_form(self):
        self.click(*self.BTN_SUBMIT)

    def verify_contact_form_submit(self):
        self.verify_two_texts_match(self.text, *self.SUCCESS_MESSAGE)
