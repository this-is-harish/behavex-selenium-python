import random
import time

from behave.runner import Context
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from pages.common_page import CommonPage


class TwitchPage(CommonPage):
    def __init__(self, context: Context):
        super().__init__(context)
        self.driver: webdriver = context.driver
        self.context: Context = context
        self.browse_button = (By.CSS_SELECTOR, "a[href='/directory']")
        self.search_bar = (By.CSS_SELECTOR, 'input[data-a-target="tw-input"]')
        self.start_watching_button = (
            By.CSS_SELECTOR,
            'button[data-a-target*="start-watching"]',
        )
        self.count = 0

    def click_browse_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.browse_button)
        ).click()

    def navigate_to_url(self, url):
        self.driver.get(url)

    def input_text_in_search_bar(self, text_to_find):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_bar)
        ).send_keys(text_to_find)
        self.driver.find_element(*self.search_bar).send_keys(Keys.ENTER)

    def click_tab_from_search_result(self, tab_name):
        locator = (By.CSS_SELECTOR, f'a[role="tab"][href*="{tab_name.lower()}"]')
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def select_random_streamer(self, retry=3):
        self.wait_for_page_to_load()
        streamer_link = (
            By.XPATH,
            f'//p[normalize-space()="{self.context.search_text}"]/preceding-sibling::div',
        )
        elements = self.driver.find_elements(*streamer_link)
        while self.count <= retry:
            try:
                element = random.choice(elements)
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(element)
                ).click()
                self.count += 1
                self.context.streamer_name = element.text
                print(f"Clicked after {self.count} tries")
                return
            except Exception as e:
                self.select_random_streamer()
                self.count += 1
                if self.count >= retry:
                    print("Max retries reached, could not select a proper streamer.")
                    return

    def click_start_watching_button(self):
        self.wait_for_page_to_load()
        try:
            if (
                WebDriverWait(self.driver, 2)
                .until(EC.element_to_be_clickable(self.start_watching_button))
                .is_displayed()
            ):
                self.driver.find_element(*self.start_watching_button).click()
        except Exception as e:
            print("May be there's no pop-up for this streamer")

    def is_video_displayed(self):
        self.wait_for_page_to_load()
        pause_button = (
            WebDriverWait(self.driver, 10)
            .until(
                EC.element_to_be_clickable(
                    self.driver.find_element(
                        By.CSS_SELECTOR,
                        '[data-a-target="player-overlay-click-handler"]',
                    )
                )
            )
            .is_displayed()
        )
        return pause_button

    def is_streamer_name_correct(self):
        return self.driver.find_element(
            By.CSS_SELECTOR, f'p[title = "{self.context.streamer_name}"]'
        ).is_displayed()
