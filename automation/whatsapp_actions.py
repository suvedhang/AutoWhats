from playwright.sync_api import Page
import time


def send_message(page: Page, contact_name: str, message: str) -> bool:
    """
    Send a WhatsApp message using search + first result click.
    NO exact title matching.
    """

    try:
        print("[DEBUG] send_message() started")

        # 1. Ensure WhatsApp UI loaded
        page.wait_for_selector("body", timeout=20000)

        # 2. Find search box (new + old UI support)
        search_box = None

        try:
            search_box = page.wait_for_selector(
                "input[placeholder*='Search']",
                timeout=5000
            )
            print("[DEBUG] Found search input by placeholder")
        except Exception:
            pass

        if search_box is None:
            try:
                search_box = page.wait_for_selector(
                    "input[aria-label*='Search']",
                    timeout=5000
                )
                print("[DEBUG] Found search input by aria-label")
            except Exception:
                pass

        if search_box is None:
            search_box = page.wait_for_selector(
                "div[role='textbox']",
                timeout=5000
            )
            print("[DEBUG] Found search box as textbox")

        # 3. Clear + type contact name
        search_box.click()
        page.keyboard.press("Control+A")
        page.keyboard.press("Backspace")
        search_box.fill(contact_name)

        page.wait_for_timeout(1500)

        # 4. CLICK FIRST SEARCH RESULT (NO NAME MATCHING)
        print("[DEBUG] Clicking first search result")
        chat = page.wait_for_selector(
            "div#pane-side span[title]",
            timeout=15000
        )
        chat.click()

        # 5. Message input box
        message_box = page.wait_for_selector(
            "footer div[contenteditable='true']",
            timeout=15000
        )

        message_box.click()
        message_box.fill(message)
        message_box.press("Enter")

        print(f"[SUCCESS] Message sent to {contact_name}")
        return True

    except Exception as e:
        print(f"[ERROR] Failed to send message: {e}")
        return False
