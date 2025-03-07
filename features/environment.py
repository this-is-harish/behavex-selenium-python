import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from dotenv import load_dotenv
from behave.runner import Context
from selenium.webdriver.support.wait import WebDriverWait

load_dotenv()


def before_scenario(context: Context, scenario):
    print(f"{scenario}--> Starting")


def before_all(context):
    logging.basicConfig(level=logging.ERROR)
    logging.getLogger("urllib3").setLevel(logging.ERROR)
    logging.getLogger("selenium.webdriver").setLevel(logging.ERROR)

    mobile_emulation = {
        "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
        "clientHints": {"platform": "Android", "mobile": True},
    }

    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_window_size(411, 731)
    context.driver = driver


def after_all(context):
    context.driver.quit()


def after_step(context, step):
    print(step.name, "->", step.status)
    WebDriverWait(context.driver, 10).until(
        lambda driver: context.driver.execute_script("return document.readyState")
        == "complete"
    )
    screenshot_name = f"{context.evidence_path}/{step.name[:50].replace(' ', '_').replace('"','')}.png"
    context.driver.save_screenshot(screenshot_name)
    print(f"Screenshot saved: {screenshot_name}")
