# Created by Owl at 10/13/19
Feature: Test for Amazon Search functionality


  Scenario: User can search for a product
    Given Open Amazon page
    When Search for shoes
    Then Search results for shoes is shown

  Scenario: User can add printer paper product into the cart
    Given Open Amazon page
    When Search for printer paper
    And Open the first product Search result
    And Click Add to cart button
    Then Verify cart has 1 item

  Scenario: User add Vital proteins collagen peptides powder product into the cart
    Given Open Amazon page
    When Search for Vital Proteins Collagen Peptides Powder
    And Open Vital Proteins Collagen Peptides Powder product Search result
    And Click Add to cart button
    And Close suggestion side section
    And Click Amazon Shopping Cart icon
    Then Verify that cart has Vital Proteins Collagen Peptides Powder item

 Scenario: User can add a product from today’s deals into the cart and then go back
   to the previous window, refresh and see cart counter has an item
   Given Open Amazon page
   When Store original windows
   And Click to open Deals under 25
   And Switch to the newly opened window
   Then Shop all deals are showing
   Then Click on any product to add it to the cart
   And User can close new window and switch back to original
   And Refresh the current page
   Then Verify cart has 1 item

