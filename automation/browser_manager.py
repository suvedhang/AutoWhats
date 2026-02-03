from playwright.sync_api import sync_playwright
import os


class BrowserManager:
    def __init__(self):
        self.playwright = sync_playwright().start()

        # Use existing persistent Chrome profile
        profile_path = os.path.abspath("storage/chrome_profile")

        self.context = self.playwright.chromium.launch_persistent_context(
            user_data_dir=profile_path,
            headless=False,
            slow_mo=300,
            args=["--start-maximized"],
        )

        # Reuse existing page if available
        if self.context.pages:
            self.page = self.context.pages[0]
        else:
            self.page = self.context.new_page()

        # Navigate to WhatsApp Web
        self.page.goto("https://web.whatsapp.com")

        print("Waiting for WhatsApp Web to load...")
        # Wait until chat list is visible (WhatsApp ready)
        self.page.wait_for_selector(
        "div#pane-side",
    timeout=12000
)

        print("WhatsApp Web ready")

    def get_page(self):
        return self.page

    def close(self):
        # IMPORTANT:
        # Do NOT close context or playwright automatically
        # This preserves WhatsApp login across runs
        pass
