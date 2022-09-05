from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage
from pages.contact_page import ContactPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.contact_page = ContactPage(self.driver)
