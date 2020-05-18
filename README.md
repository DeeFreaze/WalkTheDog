# WalkTheDog
WalkTheDog - веб-приложение(сервис) по выгулу собак.


# Интегрированные технологии:
Название технологии  | Ссылка на гит 
----------------|----------------------
django-allauth==0.41.0 | https://github.com/pennersr/django-allauth


# Описание функционала:

Действие  | Описание
----------------|----------------------
TODO:  | <Description> 
TODO:  | <Description> 
TODO:  | <Description> 
TODO:  | <Description> 
TODO:  | <Description> 
TODO:  | <Description> 
TODO:  | <Description> 
TODO:  | <Description> 
TODO:  | <Description> 
TODO:  | <Description> 


# Deploy Local:
Команда  | Описание
----------------|----------------------
docker-compose -f local.yml up      | Запускаем контейнер с работой в фоновом режиме
docker-compose -f local.yml up -d   | Запускаем контейнер с работой в реальном времени
docker-compose -f local.yml build    | Делаем build контейнера
docker-compose -f local.yml run --rm django python manage.py makemigrations    | Делаем миграции после обновления моделей
docker-compose -f local.yml run --rm django python manage.py migrate    | Делаем миграции для всего проекта
docker-compose -f local.yml run --rm django python manage.py createsuperuser  | Создаем суперпользователя
docker-compose -f local.yml ps    | Просмотр запущенных контейнеров
docker-compose -f local.yml stop   | Остановить контейнер
docker-compose -f local.yml down --volumes --rmi all   | Остановка и удаление всех данных контейнера


# Deploy Productions:
### Deploy table after deployment

