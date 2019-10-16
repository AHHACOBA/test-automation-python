# Created by Owl at 10/5/19
Feature: Tests for Orders functionality

  #Scenario: Logged out User sees "Sign in" page when clicking Orders
   #Given Open Amazon page
    #When Click Amazon Orders link
    #Then Verify Sign In page is opened

  Scenario: User clicks on the empty Shopping Cart icon and verifies it's empty
    Given Open Amazon page
    When Click Amazon Shopping Cart icon
    Then Verify that Shopping Cart is empty