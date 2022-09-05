from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC


class MainPage(Page):
    SEARCH_INPUT = (By.CSS_SELECTOR, '.input-text')
    SEARCH_SUBMIT = (By.CSS_SELECTOR, '.action.search')
    CONTACT_LINK = (By.CSS_SELECTOR, '.footer.content a[href*="contact"]')
    CART_ICON_NUMBER = (By.CSS_SELECTOR, '.counter-number')

    def open_main_page(self):
        self.open_page("https://magento.softwaretestingboard.com/")

    def input_search(self, search_word):
        self.input_text(search_word, *self.SEARCH_INPUT)

    def click_search_icon(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.SEARCH_SUBMIT))
        self.click(*self.SEARCH_SUBMIT)

    def scroll_to_contact_link(self):
        self.scroll_to_element(*self.CONTACT_LINK)

    def click_contact_link(self):
        self.click(*self.CONTACT_LINK)

    def verify_cart_icon_single_qty(self):
        self.driver.wait.until(EC.text_to_be_present_in_element(self.CART_ICON_NUMBER, '1'))
        assert '1' == self.driver.find_element(*self.CART_ICON_NUMBER).text, \
            f"Expected quantity 1 actual quantity {self.driver.find_element(*self.CART_ICON_NUMBER).text}"
