from playwright.sync_api import sync_playwright
from config.settings import WHATSAPP_WEB_URL, CHROME_PROFILE_PATH, BROWSER_HEADLESS

class BrowserManager:
    def __init__(self):
        self.playwright = sync_playwright().start()

        self.context = self.playwright.chromium.launch_persistent_context(
            user_data_dir=CHROME_PROFILE_PATH,
            headless=BROWSER_HEADLESS,
            args=["--start-maximized"]
        )

        self.page = self.context.new_page()
        self.page.goto(WHATSAPP_WEB_URL)

    def get_page(self):
        return self.page
