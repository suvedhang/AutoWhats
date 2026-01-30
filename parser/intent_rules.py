import re

SEND_MESSAGE_PATTERN = re.compile(
    r'send\s+"(.+?)"\s+to\s+(.+)',
    re.IGNORECASE
)

COUNT_UNREAD_PATTERN = re.compile(
    r'how\s+many\s+unread\s+messages',
    re.IGNORECASE
)
