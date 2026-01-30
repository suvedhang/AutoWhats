"""
Automation Controller

This module is the orchestration layer of the system.
It consumes ONLY validated, normalized command JSON produced by the agent.

Responsibilities:
- Initialize and manage the browser tool
- Route intents to the correct automation capability
- Return structured results

It does NOT:
- Parse user text
- Perform AI reasoning
- Contain UI selectors
"""

from automation.browser_manager import BrowserManager
from automation.unread_detector import count_unread_messages
from automation.whatsapp_actions import send_message


class AutomationController:
    def __init__(self):
        """
        Initialize the browser manager and obtain the active page.
        The browser manager uses a persistent Chrome profile.
        """
        self.browser = BrowserManager()
        self.page = self.browser.get_page()

    def execute(self, command_json: dict) -> dict:
        """
        Execute an automation action based on normalized command JSON.

        Args:
            command_json (dict): Validated command with intent and entities

        Returns:
            dict: Structured JSON response
        """
        intent = command_json.get("intent")
        entities = command_json.get("entities", {})

        # -------------------------------------------------
        # COUNT UNREAD MESSAGES (READ-ONLY, SAFE)
        # -------------------------------------------------
        if intent == "COUNT_UNREAD":
            unread_count = count_unread_messages(self.page)

            return {
                "status": "success",
                "intent": "COUNT_UNREAD",
                "unread_count": unread_count
            }

        # -------------------------------------------------
        # SEND MESSAGE
        # -------------------------------------------------
        if intent == "SEND_MESSAGE":
            contact = entities.get("contact")
            message = entities.get("message")

            if not contact or not message:
                return {
                    "status": "error",
                    "intent": "SEND_MESSAGE",
                    "reason": "Missing contact or message"
                }

            success = send_message(
                page=self.page,
                contact_name=contact,
                message=message
            )

            if success:
                return {
                    "status": "success",
                    "intent": "SEND_MESSAGE",
                    "contact": contact,
                    "message": message
                }

            return {
                "status": "error",
                "intent": "SEND_MESSAGE",
                "reason": "Failed to send message"
            }

        # -------------------------------------------------
        # UNKNOWN / UNSUPPORTED INTENT
        # -------------------------------------------------
        return {
            "status": "error",
            "intent": intent,
            "reason": "Unsupported or unknown intent"
        }
