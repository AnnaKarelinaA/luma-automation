# Created by annakarelina at 9/3/22
Feature: Test scenarios for search functionality


  Scenario: User can search for an item
    Given Open Luma page
    When Input Watch  into search field
    And Click on search icon
    Then URL contains search name Watch
    Then Watch is in item search result
