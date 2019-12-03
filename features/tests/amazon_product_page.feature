# Created by Owl at 11/27/19
Feature: Tests for product page

  Scenario: Size tooltip is shown upon hoovering over Add to Cart button
    Given Open Amazon product B074TBCSC8 page
    When Hoover over Add To Cart button
    Then Verify size selection tooltip is shown

  Scenario: User can select Books department (Lesson 8)
    Given Open Amazon page
    When Select Books department
    And Search for Faust
    Then Books department is selected

  Scenario: User can select any department (HW8)
    Given Open Amazon page
    When Select Pet Supplies department
    And Search for Bones
    Then Pet Supplies department is selected

  Scenario: Flyout is shown upon hoovering over Sales and Deals link
    Given Open Amazon product B074TBCSC8 page
    When Hoover over Sales and Deals link
    Then Verify Sales and Deals flyout is shown
