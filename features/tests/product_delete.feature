# Created by annakarelina at 9/3/22
Feature: Test Scenarios for Item Delete functionality
  # Enter feature description here

  Scenario: User can add multiple items and delete them in cart
    Given Open Luma page
    When Input Watch into search field
    And Click on search icon
    When Add 5 items to cart
    When Click shopping cart icon
    When Click view shopping cart
    And  Remove 5 items in cart
    Then You have no items in your shopping cart. message is shown
