import time

from behave import step
from behave.runner import Context

from pages.twitch.twitch_page import TwitchPage


@step('user navigates to "{url}"')
def navigate_to_url(context: Context, url):
    twitch_page = TwitchPage(context)
    twitch_page.navigate_to_url(url=url)
    # twitch_page.click_start_watching_button()


@step("user clicks search icon")
def user_is_on_twitch(context: Context):
    twitch_page = TwitchPage(context)
    twitch_page.click_browse_button()


@step('user searches for "{search_text}" in search bar')
def search_in_bar(context: Context, search_text):
    twitch_page = TwitchPage(context)
    context.search_text = search_text
    twitch_page.input_text_in_search_bar(text_to_find=search_text)


@step('clicks "{tab_name}" tab from search results')
def click_tab_from_search(context: Context, tab_name):
    twitch_page = TwitchPage(context)
    twitch_page.click_tab_from_search_result(tab_name=tab_name)


@step('user scrolls the page "{count}" times')
def scroll_page_n_times(context: Context, count):
    twitch_page = TwitchPage(context)
    twitch_page.scroll_page(scroll_count=int(count))


@step("user selects a random streamer")
def select_random_streamer(context: Context):
    twitch_page = TwitchPage(context)
    twitch_page.select_random_streamer()
    twitch_page.click_start_watching_button()


@step("video is played on selected streamer")
def verify_video_is_played(context: Context):
    twitch_page = TwitchPage(context)
    assert twitch_page.is_video_displayed() is True, "May be it's not displayed"
    assert twitch_page.is_streamer_name_correct() is True, "May be it's not displayed"
