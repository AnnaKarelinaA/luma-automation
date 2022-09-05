# Created by annakarelina at 9/3/22

Feature: Test Scenarios for Cart functionality


  Scenario: User can add a product and see it in cart
    Given Open Luma page
    When Input Watch into search field
    And Click on search icon
    When Add search result item to cart
    When Click shopping cart icon
    When Click view shopping cart
    Then Watch is in cart
    Then Cart item quantity equals 1


  Scenario: User can add a product to cart
    Given Open Luma page
    When Input Watch into search field
    And Click on search icon
    When Add search result item to cart
    Then Cart icon quantity with single item in cart equals 1
    Then Add to cart success message with product name is shown


  Scenario: User can add a product and see it in mini cart
    Given Open Luma page
    When Input Watch into search field
    And Click on search icon
    When Add search result item to cart
    When Click shopping cart icon
    Then Watch is in mini cart product details
    Then Mini Cart item quantity equals 1


  Scenario: User can add multiple products and see it in cart
    Given Open Luma page
    When Input Watch into search field
    And Click on search icon
    When Add 3 items to cart
    When Click shopping cart icon
    When Click view shopping cart
    Then Watch is in cart
    Then Cart icon quantity for items in cart equals 3
