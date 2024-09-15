from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

app = FastAPI()

# Функция для выполнения фоновой задачи
def background_task():
    print(f"Фоновая задача выполнена в {datetime.now()}")

# Настройка планировщика задач
scheduler = BackgroundScheduler()
scheduler.add_job(func=background_task, trigger="interval", seconds=10)
scheduler.start()