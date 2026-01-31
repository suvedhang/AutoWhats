import time
from config.selectors import SEARCH_BOX, MESSAGE_INPUT_BOX
from config.delays import human_delay


def send_message(page, contact_name: str, message: str) -> bool:
    """
    Robust message sender that works for:
    - Contacts
    - Groups
    - Emoji group names
    - Partial matches
    """

    # 1️⃣ Focus search box
    page.wait_for_selector(SEARCH_BOX, timeout=15000)
    page.click(SEARCH_BOX)
    time.sleep(human_delay())

    # 2️⃣ Clear search
    page.keyboard.press("Control+A")
    page.keyboard.press("Backspace")
    time.sleep(human_delay(200, 400))

    # 3️⃣ Type contact / group name
    page.keyboard.type(contact_name, delay=80)
    time.sleep(human_delay(1000, 1500))

    # 4️⃣ Open FIRST matched chat (works for groups)
    page.keyboard.press("Enter")
    time.sleep(human_delay(800, 1200))

    # 5️⃣ Type message
    page.wait_for_selector(MESSAGE_INPUT_BOX, timeout=15000)
    page.click(MESSAGE_INPUT_BOX)

    for char in message:
        page.keyboard.type(char)
        time.sleep(human_delay(40, 120))

    # 6️⃣ Send message
    page.keyboard.press("Enter")
    time.sleep(human_delay())

    return True
