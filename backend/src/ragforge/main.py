from fastapi import FastAPI

from ragforge.api.routes.health import router as health_router


def create_app() -> FastAPI:
    """Application factory."""

    app = FastAPI(
        title="Ragforge API",
        description=(
            "Multi-tenant platform for building,"
            "managing and evaluating RAG applications."
        ),
        version="0.1.0",
    )

    app.include_router(health_router)
    return app

app = create_app()