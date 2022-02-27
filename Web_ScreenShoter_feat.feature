Feature: Episode screenshoting automation
Scenario: Episode screenshoting automation
    Given Sign in and start the episode
    When Restart the episode
    Then Compare the slider time to be less than 1 sec 
    When Start gathering data
    Then Compare the list of screenshots files