import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.app import init_app

app = FastAPI(
    title="ATATEK - онлайн шежіре",
    version="3.0.0",
    description="Жаңа нұсқа жаңа фреймворкта FastAPI",
)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000", "https://ortalyk.worklog.kz"],  # Разрешаем фронтенду на Next.js делать запросы
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

init_app(app)


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)