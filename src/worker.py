"""Minimal resilient queue worker used by the release fixture."""


def retry_delay(attempt: int) -> int:
    """Return the bounded retry delay for an attempt."""
    return min(60, 2 ** max(0, attempt))
