# tg_days_without_coronavirus_counter
Telegram-бот, который раз в сутки отправляет сообщение с количеством дней без коронавируса.

## Dependencies
- Python 3.8.6
- Docker

## How to build and run
```bash
# Сборка контейнера
docker build -t days_without_covid .

# Запуск контейнера
docker run days_without_covid
```