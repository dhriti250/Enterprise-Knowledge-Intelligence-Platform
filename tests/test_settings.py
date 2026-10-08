"""Tests for environment-driven settings."""

import pytest
from pydantic import ValidationError

from app.config.settings import Settings


def test_settings_load_from_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    """Settings should read supported configuration from environment variables."""
    monkeypatch.setenv("APP_NAME", "Configured Platform")
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")

    settings = Settings(_env_file=None)

    assert settings.app_name == "Configured Platform"
    assert settings.log_level == "DEBUG"


def test_settings_reject_invalid_log_level(monkeypatch: pytest.MonkeyPatch) -> None:
    """Invalid log levels should fail validation rather than silently default."""
    monkeypatch.setenv("LOG_LEVEL", "VERBOSE")

    with pytest.raises(ValidationError):
        Settings(_env_file=None)
