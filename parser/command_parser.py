from parser.intent_rules import (
    SEND_MESSAGE_PATTERN,
    COUNT_UNREAD_PATTERN
)
from utils.json_builder import build_command_json

def parse_command(user_input: str):
    match = SEND_MESSAGE_PATTERN.search(user_input)
    if match:
        return build_command_json(
            intent="SEND_MESSAGE",
            contact=match.group(2).strip(),
            message=match.group(1).strip()
        )

    if COUNT_UNREAD_PATTERN.search(user_input):
        return build_command_json(intent="COUNT_UNREAD")

    return build_command_json(intent="UNKNOWN")
