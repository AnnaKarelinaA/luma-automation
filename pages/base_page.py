import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.driver.wait = WebDriverWait(self.driver, 10)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def click_wait(self, locator):
        self.driver.wait.until(EC.element_to_be_clickable(locator)).click()

    def input_text(self, text, *locator):
        input_field = self.driver.find_element(*locator)
        input_field.clear()
        input_field.send_keys(text)

    def input_text_wait(self, text, *locator):
        self.driver.wait.until(EC.visibility_of_element_located(locator))
        input_field = self.driver.find_element(*locator)
        input_field.clear()
        input_field.send_keys(text)

    def open_page(self, url):
        self.driver.get(url)

    def dropdown_select_by_int_value(self, start_value, end_value, *locator):
        self.driver.find_element(*locator).click()
        select = Select(self.driver.find_element(*locator))
        select.select_by_value(str(random.randint(start_value, end_value)))

    def dropdown_select_by_str_value(self, value_str: str, *locator):
        self.driver.find_element(*locator).click()
        select = Select(self.driver.find_element(*locator))
        select.select_by_value(value_str)

    def scroll_to_element(self, *locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('return arguments[0].scrollIntoView(true);', element)

    def verify_two_texts_match(self, expected_text, *locator):
        assert expected_text == self.driver.find_element(*locator).text, \
            f"Expected {expected_text} Actual {self.driver.find_element(*locator).text}"

    def verify_text_contains(self, key_word, *locator):
        assert key_word in self.driver.find_element(*locator).text, \
            f"Expected query {key_word} not in {self.driver.find_element(*locator).text}"

    def verify_url_contains(self, key_word):
        assert key_word.lower() in self.driver.current_url.lower(), \
            f"Expected {key_word} not in {self.driver.current_url.lower()}"
