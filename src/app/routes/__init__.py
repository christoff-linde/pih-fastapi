"""Entrypoint for all routes in the module."""

from fastapi import APIRouter
from app.routes import client


router = APIRouter()
router.include_router(client.router)


@router.get("/")
def root() -> str:
    return "Hello, World!"
