ALLOWED_INTENTS = {"SEND_MESSAGE", "COUNT_UNREAD"}

def validate_command_json(command: dict) -> bool:
    if not isinstance(command, dict):
        return False

    if "intent" not in command or "entities" not in command:
        return False

    if command["intent"] not in ALLOWED_INTENTS:
        return False

    entities = command["entities"]
 
    if not isinstance(entities, dict):
        return False

    if command["intent"] == "SEND_MESSAGE":
        return bool(entities.get("contact")) and bool(entities.get("message"))

    return True
