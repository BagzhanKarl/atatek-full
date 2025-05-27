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

# Обработка HTTP ошибок
from fastapi.exceptions import HTTPException
app.add_exception_handler(HTTPException, http_exception_handler)

# Обработка ошибок валидации (например, pydantic)
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={
            "status": "error",
            "version": "1.0.0",
            "data": {"detail": exc.errors()}
        }
    )



init_app(app)


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)