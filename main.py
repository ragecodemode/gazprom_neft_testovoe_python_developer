import uvicorn
from fastapi import FastAPI

from app.routers.routers import measurements_routes

app = FastAPI(title="Система учета и анализа данных")

app.include_router(measurements_routes)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
