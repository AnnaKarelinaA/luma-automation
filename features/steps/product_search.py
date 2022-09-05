from selenium.webdriver.common.by import By
from behave import *
SEARCH_RESULT_ITEM_NAME = (By.CSS_SELECTOR, '.product-item-name:nth-of-type(1)')


@then('{search_word} is in item search result')
def verify_search_result(context, search_word):
    context.app.search_page.verify_item_name_in_product_results(search_word)
