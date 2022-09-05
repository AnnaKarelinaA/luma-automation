from selenium.webdriver.common.by import By
from pages.base_page import Page


class ProductPage(Page):
    ADD_TO_CART = (By.ID, 'product-addtocart-button')

    def add_item_to_cart(self):
        self.click(*self.ADD_TO_CART)
