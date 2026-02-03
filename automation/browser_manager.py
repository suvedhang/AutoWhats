from playwright.sync_api import sync_playwright


class BrowserManager:
    def __init__(self):
        self.playwright = sync_playwright().start()

        # Launch normal browser (NOT persistent context)
        self.browser = self.playwright.chromium.launch(
            headless=False,
            slow_mo=300,
            args=["--start-maximized"],
        )

        # Create a browser context
        self.context = self.browser.new_context()

        # Open a new page
        self.page = self.context.new_page()

        # Navigate to WhatsApp Web
        self.page.goto("https://web.whatsapp.com")

    def get_page(self):
        return self.page

    def close(self):
        try:
            self.context.close()
        except Exception:
            pass

        try:
            self.browser.close()
        except Exception:
            pass

        try:
            self.playwright.stop()
        except Exception:
            pass
