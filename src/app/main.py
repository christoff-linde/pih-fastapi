"""The main entrypoint for the FastAPI Application."""
from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="pih-fastapi-backend",
    description=(
        "A simple FastAPI backend used for local development of the PIH system."
    ),
)

app.include_router(router)
