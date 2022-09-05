# Created by annakarelina at 9/3/22
Feature: Test Scenarios for purchase functionality


  Scenario: User can purchase an item
    Given Open Luma page
    When Input Watch into search field
    When Click on search icon
    And Click on first item
    When Add item to cart
    And Click shopping cart icon
    And Click view shopping cart
    And Click "Proceed to Checkout"
    When Input Shipping Address
    When Select Shipping Method
    When Click Next
    And Click Place Order
    Then Order ID is shown
    Then Success is in URL
    Then "Thank you for your purchase!" is shown
