Feature: OrangeHRM logo
  Scenario: Validate logo presence on Home page
    Given launch chrome browser
    When open orangeHRM home page
    Then orangeHRM logo should be present on page
    And close browser