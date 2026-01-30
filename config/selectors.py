"""
Centralized UI selectors for WhatsApp Web.

All selectors are kept here to:
- Avoid scattering selectors across logic
- Make UI changes easy to fix
- Maintain clean separation of concerns
"""

# =========================
# PAGE / APP LEVEL
# =========================

# Main WhatsApp Web container (used to ensure page is loaded)
APP_CONTAINER = 'div[id="app"]'


# =========================
# CHAT LIST (LEFT PANEL)
# =========================

# Chat list container
CHAT_LIST = 'div[aria-label="Chat list"]'

# Individual chat title (contact / group name)
CHAT_TITLE = 'span[title]'

# Unread message badge (green number)
# This appears only if a chat has unread messages
UNREAD_BADGE = 'span[data-testid="icon-unread-count"]'


# =========================
# SEARCH
# =========================

# Search box to find a contact or group
# (contenteditable div used by WhatsApp)
SEARCH_BOX = 'div[contenteditable="true"][data-tab="3"]'


# =========================
# CHAT WINDOW (RIGHT PANEL)
# =========================

# Message input box inside an opened chat
MESSAGE_INPUT_BOX = 'div[contenteditable="true"][data-tab="10"]'

# Send button (used only as fallback; Enter key preferred)
SEND_BUTTON = 'button[data-testid="compose-btn-send"]'


# =========================
# STATUS / SAFETY
# =========================

# QR code canvas (only appears if not logged in)
QR_CODE_CANVAS = 'canvas[aria-label="Scan me!"]'

# Loading spinner (WhatsApp initial load)
LOADING_SPINNER = 'progress'


# =========================
# MISC / FUTURE USE
# =========================

# Top bar of an opened chat (contains contact info)
CHAT_HEADER = 'header[data-testid="conversation-header"]'
