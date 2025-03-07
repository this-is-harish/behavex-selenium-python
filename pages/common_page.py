import time

from behave.runner import Context
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait


class CommonPage:
    def __init__(self, context: Context):
        self.context = context

    def wait_for_page_to_load(self):
        WebDriverWait(self.context.driver, 10).until(
            lambda driver: self.context.driver.execute_script(
                "return document.readyState"
            )
            == "complete"
        )

    def scroll_page(self, scroll_count: int = 2):
        actions = ActionChains(self.context.driver)
        for _ in range(scroll_count):
            self.wait_for_page_to_load()
            actions.send_keys(Keys.SPACE).perform()
            time.sleep(1)
