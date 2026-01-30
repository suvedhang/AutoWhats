def gemini_agent(user_input: str) -> dict:
    user_input = user_input.lower()

    if "send" in user_input and "to" in user_input:
        parts = user_input.split("to")
        message = parts[0].replace("send", "").strip()
        contact = parts[1].strip()

        return {
            "intent": "SEND_MESSAGE",
            "entities": {
                "contact": contact.title(),
                "message": message
            }
        }

    if "unread" in user_input:
        return {
            "intent": "COUNT_UNREAD",
            "entities": {
                "contact": None,
                "message": None
            }
        }

    return {
        "intent": "UNKNOWN",
        "entities": {
            "contact": None,
            "message": None
        }
    }
