"""Tests for the application API foundation."""

from fastapi.testclient import TestClient

from app.config.settings import Settings
from app.main import create_app


def test_health_endpoint_reports_liveness() -> None:
    """The health endpoint should identify a running API process."""
    application = create_app(Settings())

    with TestClient(application) as client:
        response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_app_title_uses_configured_setting() -> None:
    """The OpenAPI metadata should use the configured application name."""
    application = create_app(Settings(app_name="Test Knowledge Platform"))

    assert application.title == "Test Knowledge Platform"
