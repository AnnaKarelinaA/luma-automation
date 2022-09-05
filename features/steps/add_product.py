from time import sleep
from behave import *


@given('Open Luma page')
def open_luma(context):
    context.app.main_page.open_main_page()


@when('Input {search_word} into search field')
def input_search(context, search_word):
    context.app.main_page.input_search(search_word)


@when('Click on search icon')
def click_search_icon(context):
    context.app.main_page.click_search_icon()


@then('Search results for {search_word} are shown')
def verify_search_results_shown(context, search_word):
    context.app.search_page.verify_item_name_in_product_results(search_word)


@then('URL contains search name {search_word}')
def verify_search_word_url(context, search_word):
    context.app.search_page.verify_search_item_name_in_url(search_word)


@when('Add search result item to cart')
def add_found_result_item_to_cart(context):
    context.app.search_page.add_single_product_to_cart()


@then('Add to cart success message with product name is shown')
def verify_add_to_cart_message(context):
    context.app.search_page.verify_add_to_cart_text()


@when('Click shopping cart icon')
def click_on_cart(context):
    sleep(2)  # TODO unstable button
    context.app.search_page.click_cart()


@then('{item_name} is in mini cart product details')
def verify_product_in_mini_cart(context, item_name):
    context.app.search_page.verify_item_name_in_mini_cart(item_name)


@when('Click view shopping cart')
def view_cart(context):
    context.app.search_page.click_view_edit_cart()


@then('{product_name} is in cart')
def verify_added_item_in_cart(context, product_name):
    context.app.cart_page.verify_item_name(product_name)


@then('Cart icon quantity for items in cart equals {item_quantity}')
def verify_cart_icon_number(context, item_quantity):
    context.app.cart_page.verify_cart_icon_qty(item_quantity)


@then('Cart icon quantity with single item in cart equals 1')
def verify_cart_icon_number(context):
    context.app.main_page.verify_cart_icon_single_qty()


@then('Cart item quantity equals {item_quantity}')
def verify_cart_item_qty(context, item_quantity):
    context.app.cart_page.verify_cart_item_quantity(item_quantity)


@then('Mini Cart item quantity equals {item_quantity}')
def verify_item_count_mini_cart(context, item_quantity):
    context.app.cart_page.verify_minicart_item_quantity(item_quantity)


@when('Add {number} items to cart')
def add_multiple_items(context, number):
    context.app.search_page.add_multiple_products_to_cart(number)
