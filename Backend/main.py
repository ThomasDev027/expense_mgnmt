from fastapi import FastAPI

from routes.router import api_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Expense Manager API",
        version="1.0.0",
    )

    app.include_router(api_router)

    return app


app = create_app()
