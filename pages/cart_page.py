from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC


class CartPage(Page):
    DELETE_ICON = (By.CSS_SELECTOR, '.action.action-delete')
    ITEM_CHECKOUT = (By.CSS_SELECTOR, '.item button.primary.checkout')
    CART_EMPTY = (By.CSS_SELECTOR, '.cart-empty > p')
    CART_ITEM_TEXT = (By.CSS_SELECTOR, '.product-item-name')
    CART_ITEM_QTY = (By.CSS_SELECTOR, 'input[name*="qty"]')
    CART_ICON_NUMBER = (By.CSS_SELECTOR, '.counter-number')
    MINI_CART_ITEM_COUNTER = (By.CSS_SELECTOR, '.count')
    ITEMS_COUNT = (By.CSS_SELECTOR, '#shopping-cart-table .cart.item')

    def click_proceed_checkout(self):
        self.click_wait(self.ITEM_CHECKOUT)

    def delete_items(self, item_quantity):
        items = int(item_quantity) - 1
        while items >= 0:
            delete_icons = self.driver.find_elements(*self.DELETE_ICON)
            delete_icons[items].click()
            items -= 1

    def verify_empty_cart_text(self, text):
        self.verify_two_texts_match(text, *self.CART_EMPTY)

    def verify_item_name(self, product_name):
        self.driver.wait.until(EC.text_to_be_present_in_element(self.CART_ITEM_TEXT, product_name))
        self.verify_text_contains(product_name, *self.CART_ITEM_TEXT)

    def verify_cart_icon_qty(self, item_qty):
        #needed implement this step
        item_quantity = len(self.driver.find_elements(*self.CART_ITEM_QTY))
        self.driver.wait.until(EC.text_to_be_present_in_element(self.CART_ICON_NUMBER, str(item_quantity)))
        assert item_quantity == int(self.driver.find_element(*self.CART_ICON_NUMBER).text), \
            f"Expected quantity {item_qty} actual quantity {self.driver.find_element(*self.CART_ICON_NUMBER).text}"

    def verify_cart_item_quantity(self, item_quantity):
        assert item_quantity == self.driver.find_element(*self.CART_ITEM_QTY).get_attribute('value'), \
            f"Expected quantity {item_quantity} " \
            f"actual quantity {self.driver.find_element(*self.CART_ITEM_QTY).get_attribute('value')}"

    def verify_minicart_item_quantity(self, item_quantity):
        assert item_quantity == self.driver.find_element(*self.MINI_CART_ITEM_COUNTER).text, \
            f"Expected quantity {item_quantity} " \
            f"actual quantity {self.driver.find_element(*self.MINI_CART_ITEM_COUNTER).text}"
