from behave import *


@when('Navigate to Contact link')
def scroll_to_contact_link(context):
    context.app.main_page.scroll_to_contact_link()


@when('Click Contact us link')
def click_contact_us_link(context):
    context.app.main_page.click_contact_link()


@when('Complete Contact us form')
def complete_contact_us_form(context):
    context.app.contact_page.complete_contact_form()


@when('Submit message')
def click_submit(context):
    context.app.contact_page.submit_contact_form()


@then('Success message is shown')
def verify_success_message(context):
    context.app.contact_page.verify_contact_form_submit()
