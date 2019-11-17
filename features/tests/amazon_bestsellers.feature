# Created by Owl at 11/11/19
Feature: Test for Amazon Best Sellers page functionality


  Scenario: User can click top links to verify correct pages opens
    Given Open Amazon page
    When Clicks on Best Sellers link on the top menu
    Then Clicks on each top link and verify that new page opens
