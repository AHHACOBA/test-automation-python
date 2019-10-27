# Created by Owl at 10/24/19
Feature: Test for clothes selection


  Scenario: User can loop through dress colors
    Given Open Amazon product B07K16Z8LH page
    Then Verify user can select through colors

  Scenario: User can loop through jean colors
    Given Open Amazon product B07BKD8JCQ page
    Then Verify user can select through colors