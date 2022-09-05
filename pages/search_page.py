from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC


class SearchPage(Page):
    SEARCH_RESULT_TEXT = (By.CSS_SELECTOR, 'h1')
    SEARCH_RESULT_ITEMS = (By.CSS_SELECTOR, '.product-items .product-item')
    BTN_TO_CART = (By.CSS_SELECTOR, '.action.tocart.primary')
    PRODUCT_LINKS = (By.CSS_SELECTOR, '.product-item-link')
    CART_ICON_NUMBER = (By.CSS_SELECTOR, '.counter-number')
    SEARCH_RESULT_ITEM_NAME = (By.CSS_SELECTOR, '.product-item-link')
    ADD_TO_CART_MSG = (By.CSS_SELECTOR, 'div[class="messages"] > div > div')
    CART_ICON = (By.CSS_SELECTOR, '.showcart')
    MINI_CART_ITEM_TEXT = (By.CSS_SELECTOR, '#mini-cart .product-item-name')
    VIEW_CART = (By.CSS_SELECTOR, '.action.viewcart')

    def click_first_search_result_item(self):
        self.click(*self.PRODUCT_LINKS)

    def verify_item_name_in_product_results(self, search_word):
        self.verify_text_contains(search_word, *self.SEARCH_RESULT_TEXT)

    def verify_search_item_name_in_url(self, search_word):
        self.verify_url_contains(search_word)

    def add_single_product_to_cart(self):
        self.driver.wait.until(EC.element_to_be_clickable(self.SEARCH_RESULT_ITEMS))
        action_chain = ActionChains(self.driver)
        item = self.driver.find_element(*self.SEARCH_RESULT_ITEMS)
        action_chain.move_to_element(item).perform()
        self.click(*self.BTN_TO_CART)

    def add_multiple_products_to_cart(self, number):
        self.driver.wait.until(EC.element_to_be_clickable(self.SEARCH_RESULT_ITEMS))
        items = self.driver.find_elements(*self.SEARCH_RESULT_ITEMS)
        for item in range(0, int(number)):
            add_item = items[item]
            action_chain = ActionChains(self.driver)
            action_chain.move_to_element(add_item).perform()
            self.driver.find_elements(*self.BTN_TO_CART)[item].click()
            self.driver.wait.until(EC.text_to_be_present_in_element(self.CART_ICON_NUMBER, str(item + 1)))

    def verify_add_to_cart_text(self):
        added_item = self.driver.find_element(*self.SEARCH_RESULT_ITEM_NAME).text
        assert f"You added {added_item} to your shopping cart." in self.driver.find_element(*self.ADD_TO_CART_MSG).text, \
            f"Expected text 'You added {added_item} to your shopping cart.' " \
            f"not in {self.driver.find_element(*self.ADD_TO_CART_MSG).text}"

    def click_cart(self):
        self.click(*self.CART_ICON)

    def verify_item_name_in_mini_cart(self, item_name):
        self.verify_text_contains(item_name, *self.MINI_CART_ITEM_TEXT)

    def click_view_edit_cart(self):
        self.click(*self.VIEW_CART)
