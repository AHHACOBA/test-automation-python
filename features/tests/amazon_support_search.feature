# Created by Owl at 10/15/19
Feature: Tests for Amazon Support Search functionality
  # H W 3

  Scenario: User can search for Cancelling an Order on Amazon
   Given Open Amazon Help page
   When Search Cancel order
   And Click Go
   Then Verify that Cancel Items or Orders text is present