"""
Unread message detection module.

This module provides read-only functionality to detect
the number of chats with unread messages on WhatsApp Web.
"""

from config.selectors import UNREAD_BADGE


def count_unread_messages(page) -> int:
    """
    Count the number of chats with unread messages.

    Args:
        page: Playwright page instance

    Returns:
        int: Number of unread chats
    """
    # Allow WhatsApp UI to fully load
    page.wait_for_timeout(2000)

    unread_elements = page.query_selector_all(UNREAD_BADGE)
    return len(unread_elements)
