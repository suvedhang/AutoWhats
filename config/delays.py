"""
Human-like delay utilities.

Used to simulate realistic interaction timing
and reduce automation detection risk.
"""

import random


def human_delay(min_ms: int = 300, max_ms: int = 900) -> float:
    """
    Generate a human-like random delay.

    Args:
        min_ms (int): Minimum delay in milliseconds
        max_ms (int): Maximum delay in milliseconds

    Returns:
        float: Delay in seconds
    """
    return random.uniform(min_ms / 1000, max_ms / 1000)
