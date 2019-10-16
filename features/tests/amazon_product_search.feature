# Created by Owl at 10/13/19
Feature: Test for Amazon Search functionality


  Scenario: User can search for a product
    Given Open Amazon page
    When Search for shoes
    Then Search results for shoes is shown
