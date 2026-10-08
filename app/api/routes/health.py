"""Health-check API route."""

from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/health", tags=["health"])


class HealthResponse(BaseModel):
    """Liveness response; dependency readiness is reported separately later."""

    status: Literal["ok"]


@router.get("", response_model=HealthResponse)
def health_check() -> HealthResponse:
    """Report that the API process is serving requests."""
    return HealthResponse(status="ok")
