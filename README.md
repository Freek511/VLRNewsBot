# VLRNewsBot - simple bot for Valorant lineups
# EN
## Structure

* `main.py`: bot's codebase
* `Dockerfile`: the file to build the bot image.
* `docker-compose.yml`: used to start the bot.
* `requirements.txt`: used to specify your dependencies.

## How to deploy the bot

1. Clone or fork this repo.
2. Go to project's directory in your CMD
3. Run `docker build -t bot .`
4. Run `docker-compose up -d` and wait for the build to finish.

That's it. Enjoy your dockerized bot. 🚀

# RU
## Структура

* `main.py`: код телеграмм-бота.
* `Dockerfile`: файл, который необходим для создания docker-образа бота.
* `docker-compose.yml`: используется для запуска бота.
* `requirements.txt`: используется для определения зависимостей.

## Как развернуть бота

1. Клонируйте данный репозиторий.
2. Перейдите в каталог проекта в вашем CMD.
3. Выполните команду `docker build -t bot .`
4. Выполните команду `docker-compose up -d` и подождите, пока сборка завершиться.

Готово. Наслаждайтесь работой телеграмм-бота. 🚀
