# Created by annakarelina at 9/3/22
Feature: Test Scenarios for Contact functionality
  # Enter feature description here

  Scenario: User can send a contact us message
    Given Open Luma page
    When Navigate to Contact link
    And Click Contact us link
    When Complete Contact us form
    And Submit message
    Then Success message is shown
