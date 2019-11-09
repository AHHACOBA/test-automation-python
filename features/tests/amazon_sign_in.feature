# Created by Owl at 11/7/19
Feature: Tests for Sign In functionality
  # Enter feature description here

  Scenario: Sign In page can be opened by clicking on Sign In tooltip
    Given Open Amazon page
    When Click on Sign In btn from Sign In tooltip
    Then Verify Sign In page is opened

  Scenario: Sign In tooltip appears and disappears
    Given Open Amazon page
    Then Verify Sign In tooltip is present and clickable
    When Wait until Sign In tooltip disappears
    Then Verify Sign In tooltip is not clickable
