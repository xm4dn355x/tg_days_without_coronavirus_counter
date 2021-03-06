# Базовый образ с Python 3.8
FROM python:3.8.6-slim-buster

# Создание рабочей директории
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app/

# Установка Python зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Запуск скрипта
ENTRYPOINT ["python"]
CMD ["main.py"]