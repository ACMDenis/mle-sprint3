# импортируем класс для создания экземпляра FastAPI-приложения
from fastapi import FastAPI
import random

# создаём экземпляр FastAPI-приложения
app = FastAPI()

@app.get("/api/credit/{client_id}")
def is_credit_approved(client_id: str) -> dict:
    """Определяет одобрение кредита на основе случайного кредитного рейтинга"""
    score = random.uniform(0, 1)
    return {"approved": 1} if score > 0.8 else {"approved": 0}