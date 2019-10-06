# Created by Owl at 10/5/19
Feature: Logged out User sees "Sign in" page when clicking Orders

  Scenario: User can log in after clicking on Orders link
    Given Open Amazon page
    Then Click on Orders link
    When Sign-in page are open
    Then Verify that page opened