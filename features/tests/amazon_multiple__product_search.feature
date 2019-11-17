# Created by Owl at 11/15/19
Feature: Multiple product search

  Scenario Outline: User can search for multiple products
    Examples:
    |keyword   |expected_results   |
    |dress     |"dress"            |
    |shoes     |"shoes"            |
    |toys      |"toys"             |

    Given Open Amazon page
    When Search for <keyword>
    Then Search results for <expected_results> is shown