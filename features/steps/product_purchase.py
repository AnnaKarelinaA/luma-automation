from behave import *


@when('Click on first item')
def click_first_item(context):
    context.app.search_page.click_first_search_result_item()


@when('Add item to cart')
def add_to_cart(context):
    context.app.product_page.add_item_to_cart()


@when('Click "Proceed to Checkout"')
def click_checkout(context):
    context.app.cart_page.click_proceed_checkout()


@when('Input Shipping Address')
def input_shipping_info(context):
    context.app.checkout_page.complete_shipping_address()


@when('Select Shipping Method')
def select_shipping(context):
    context.app.checkout_page.select_shipping_method()


@when('Click Next')
def click_next(context):
    context.app.checkout_page.click_proceed_next()


@when('Click Place Order')
def click_place_order(context):
    context.app.checkout_page.click_order()


@then('Order ID is shown')
def verify_order_id_shown(context):
    context.app.checkout_page.verify_order_id()


@then('{key_word} is in URL')
def verify_text_in_url(context, key_word):
    context.app.checkout_page.verify_key_word_present_url(key_word)


@then('"{success_text}" is shown')
def verify_success_text(context, success_text):
    context.app.checkout_page.verify_success_purchase_text(success_text)
