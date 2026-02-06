from actions.unread import get_unread_breakdown

def execute_intent(intent, entities, page):
    if intent == "COUNT_UNREAD":
        breakdown = get_unread_breakdown(page)
        return {
            "status": "success",
            "intent": intent,
            "data": breakdown
        }

    return {
        "status": "error",
        "reason": "UNKNOWN_INTENT"
    }
