"""Tests for structured application logging."""

import json
import logging

from app.observability.logging import JsonFormatter


def test_json_formatter_emits_structured_record() -> None:
    """Log output should contain timestamp, severity, logger, and message fields."""
    record = logging.LogRecord(
        name="app.test",
        level=logging.INFO,
        pathname=__file__,
        lineno=1,
        msg="request accepted",
        args=(),
        exc_info=None,
    )

    payload = json.loads(JsonFormatter().format(record))

    assert payload["level"] == "INFO"
    assert payload["logger"] == "app.test"
    assert payload["message"] == "request accepted"
    assert "timestamp" in payload
