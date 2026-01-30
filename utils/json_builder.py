def build_command_json(intent, contact=None, message=None):
    return {
        "intent": intent,
        "entities": {
            "contact": contact,
            "message": message
        }
    }
