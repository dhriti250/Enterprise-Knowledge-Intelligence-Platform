"""FastAPI application factory and ASGI entry point."""

from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.config.settings import Settings, get_settings
from app.observability.logging import configure_logging


def create_app(settings: Settings | None = None) -> FastAPI:
    """Create the API application with validated runtime settings."""
    app_settings = settings or get_settings()
    configure_logging(app_settings.log_level)

    application = FastAPI(title=app_settings.app_name, version="0.1.0")
    application.include_router(health_router)
    return application


app = create_app()
