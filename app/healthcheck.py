# импортируем класс для создания экземпляра FastAPI-приложения
from fastapi import FastAPI

# создаём экземпляр FastAPI-приложения
app = FastAPI()

# обработка GET-запросов к URL /service-status
@app.get("/service-status")
def health_check() -> dict:
    return {"status": "ok"}