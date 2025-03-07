Feature: Twitch Search

  @browse_video
  Scenario: Verify if user is able to play searched video
    Given user navigates to "https://m.twitch.tv"
    And user clicks search icon
    And user searches for "StarCraft II" in search bar
    And clicks "Channels" tab from search results
    And user scrolls the page "2" times
    And user selects a random streamer
    Then video is played on selected streamer