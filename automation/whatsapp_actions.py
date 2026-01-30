import time
from config.selectors import SEARCH_BOX, CHAT_TITLE, MESSAGE_INPUT_BOX
from config.delays import human_delay


def send_message(page, contact_name: str, message: str) -> bool:
    """
    Send a message to a specific contact on WhatsApp Web.

    Args:
        page: Playwright page instance
        contact_name (str): Contact or group name
        message (str): Message text

    Returns:
        bool: True if message sent successfully
    """

    # 1️⃣ Focus search box
    page.wait_for_selector(SEARCH_BOX, timeout=15000)
    page.click(SEARCH_BOX)
    time.sleep(human_delay())

    # 2️⃣ Clear & type contact name
    page.keyboard.press("Control+A")
    page.keyboard.press("Backspace")
    page.type(SEARCH_BOX, contact_name, delay=80)
    time.sleep(human_delay(600, 1200))

    # 3️⃣ Click chat from results
    page.wait_for_selector(f'{CHAT_TITLE}[title="{contact_name}"]', timeout=15000)
    page.click(f'{CHAT_TITLE}[title="{contact_name}"]')
    time.sleep(human_delay(800, 1400))

    # 4️⃣ Type message (human-like)
    page.wait_for_selector(MESSAGE_INPUT_BOX, timeout=15000)
    page.click(MESSAGE_INPUT_BOX)

    for char in message:
        page.keyboard.type(char)
        time.sleep(human_delay(40, 120))

    time.sleep(human_delay(300, 600))

    import time
from config.selectors import SEARCH_BOX, MESSAGE_INPUT_BOX
from config.delays import human_delay


def send_message(page, contact_name: str, message: str) -> bool:
    """
    Robust message sender that does NOT rely on exact contact title match.
    """

    # 1️⃣ Focus search box
    page.wait_for_selector(SEARCH_BOX, timeout=15000)
    page.click(SEARCH_BOX)
    time.sleep(human_delay())

    # 2️⃣ Clear search box
    page.keyboard.press("Control+A")
    page.keyboard.press("Backspace")
    time.sleep(human_delay(200, 400))

    # 3️⃣ Type contact name
    page.keyboard.type(contact_name, delay=80)
    time.sleep(human_delay(1000, 1500))

    # 4️⃣ Press Enter to open first result
    page.keyboard.press("Enter")
    time.sleep(human_delay(800, 1200))

    # 5️⃣ Type message
    page.wait_for_selector(MESSAGE_INPUT_BOX, timeout=15000)
    page.click(MESSAGE_INPUT_BOX)

    for char in message:
        page.keyboard.type(char)
        time.sleep(human_delay(40, 120))

    time.sleep(human_delay(300, 600))

    # 6️⃣ Send message
    page.keyboard.press("Enter")
    time.sleep(human_delay())

    return True

    
