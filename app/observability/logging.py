"""Structured JSON logging for application modules."""

import json
import logging
import sys
from datetime import datetime, timezone

from app.config.settings import LogLevel

_HANDLER_MARKER = "_enterprise_knowledge_json_handler"


class JsonFormatter(logging.Formatter):
    """Format log records as one JSON object per line."""

    def format(self, record: logging.LogRecord) -> str:
        payload: dict[str, object] = {
            "timestamp": datetime.fromtimestamp(record.created, timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        if record.exc_info:
            payload["exception"] = self.formatException(record.exc_info)
        return json.dumps(payload, ensure_ascii=False)


def configure_logging(level: LogLevel) -> None:
    """Configure a single structured handler for the application logger."""
    application_logger = logging.getLogger("app")
    application_logger.setLevel(level)
    application_logger.propagate = False

    if not any(getattr(handler, _HANDLER_MARKER, False) for handler in application_logger.handlers):
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(JsonFormatter())
        setattr(handler, _HANDLER_MARKER, True)
        application_logger.addHandler(handler)
