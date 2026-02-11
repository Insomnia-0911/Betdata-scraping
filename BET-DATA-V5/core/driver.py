from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class SafeDriver:
    def __init__(
        self,
        headless=True,
        incognito=True,
        block_images=True,
        timeout=20
    ):
        self.timeout = timeout
        self.driver = Driver(
            browser="chrome",
            uc=False,
            headless=headless,
            incognito=incognito,
            block_images=block_images,
            disable_csp=True
        )

    def get(self, url, wait_css=None):
        self.driver.get(url)
        if wait_css:
            try:
                WebDriverWait(self.driver, self.timeout).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, wait_css))
                )
            except:
                pass

    def wait(self, seconds=1):
        time.sleep(seconds)

    def quit(self):
        try:
            self.driver.quit()
        except:
            pass
