from playwright.sync_api import sync_playwright


class BrowserManager:
    def __init__(self):
        self.playwright = sync_playwright().start()

        self.context = self.playwright.chromium.launch_persistent_context(
            user_data_dir="storage/chrome_profile",
            headless=False,
            args=["--start-maximized"],
        )

        if self.context.pages:
            self.page = self.context.pages[0]
        else:
            self.page = self.context.new_page()

        self.page.goto("https://web.whatsapp.com")

    def get_page(self):
        return self.page

    def close(self):
        self.context.close()
        self.playwright.stop()
