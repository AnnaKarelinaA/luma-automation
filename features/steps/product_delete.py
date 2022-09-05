from behave import *


@when('Remove {item_quantity} items in cart')
def delete_item_in_cart(context, item_quantity):
    context.app.cart_page.delete_items(item_quantity)


@then('{empty_cart_text} message is shown')
def verify_cart_is_empty(context, empty_cart_text):
    context.app.cart_page.verify_empty_cart_text(empty_cart_text)
