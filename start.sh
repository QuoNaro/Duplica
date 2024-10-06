#!/bin/bash

# Установка Poetry
if ! command -v poetry &> /dev/null
then
    echo "Poetry не установлен. Устанавливаем..."
    curl -sSL https://install.python-poetry.org | python3 -
fi

# Создание нового проекта
PROJECT_NAME="duplica"
if [ ! -d "$PROJECT_NAME" ]; then
    echo "Создаем новый проект $PROJECT_NAME..."
    poetry new $PROJECT_NAME
fi

cd $PROJECT_NAME

# Проверка на установленность FastAPI и Uvicorn
if ! poetry show fastapi &> /dev/null; then
    echo "FastAPI не установлен. Устанавливаем..."
    poetry add fastapi[standard]
fi

if ! poetry show uvicorn &> /dev/null; then
    echo "Uvicorn не установлен. Устанавливаем..."
    poetry add uvicorn[standard]
fi

# Запуск сервера
echo "Запускаем сервер FastAPI..."
poetry run uvicorn main:app --reload