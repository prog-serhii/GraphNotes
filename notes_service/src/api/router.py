from typing import Any

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends


router = APIRouter()


def dependency(provider) -> Any:
    return Depends(Provide[provider])
