# Created by Owl at 10/27/19
Feature: Test to verify Whole Foods deals page functionality

  Scenario: User can verify, every product on the page has a text 'Regular' and product name
    Given Open Amazon WholeFoodsDeals page
    Then Verify every product on the page has a text Regular and product name
