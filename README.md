# WalkTheDog
WalkTheDog - веб-приложение(сервис) по выгулу собак.


# Интегрированные технологии:
Название технологии  | Ссылка на гит 
----------------|----------------------
django-allauth==0.41.0 | https://github.com/pennersr/django-allauth
whitenoise==5.0.1  | https://github.com/evansd/whitenoise
redis==3.5.0  | https://github.com/andymccurdy/redis-py
hiredis==1.0.1  | https://github.com/redis/hiredis-py
celery==4.4.2  pyup: < 5.0  | https://github.com/celery/celery
django-celery-beat==2.0.0  | https://github.com/celery/django-celery-beat
flower==0.9.4  | https://github.com/mher/flower
django-widget-tweaks | https://github.com/jazzband/django-widget-tweaks
easy_thumbnails | https://github.com/SmileyChris/easy-thumbnails
beautifulsoup4==4.9.0 | https://github.com/getanewsletter/BeautifulSoup4
django==3.0.5  # pyup: < 3.1  | https://www.djangoproject.com/
django-environ==0.4.5  | https://github.com/joke2k/django-environ
django-model-utils==4.0.0  | https://github.com/jazzband/django-model-utils
django-allauth==0.41.0  | https://github.com/pennersr/django-allauth
django-crispy-forms==1.9.0  | https://github.com/django-crispy-forms/django-crispy-forms
django-compressor==2.4  | https://github.com/django-compressor/django-compressor


# Deploy Local:
Команда  | Описание
----------------|----------------------
docker-compose -f local.yml up -d    | Запускаем контейнер с работой в фоновом режиме
docker-compose -f local.yml up       | Запускаем контейнер с работой в реальном времени
docker-compose -f local.yml build    | Делаем build контейнера
docker-compose -f local.yml run --rm django python manage.py makemigrations    | Делаем миграции после обновления моделей
docker-compose -f local.yml run --rm django python manage.py migrate    | Делаем миграции для всего проекта
docker-compose -f local.yml run --rm django python manage.py createsuperuser  | Создаем суперпользователя
docker-compose -f local.yml ps    | Просмотр запущенных контейнеров
docker-compose -f local.yml stop   | Остановить контейнер
docker-compose -f local.yml down --volumes --rmi all   | Остановка и удаление всех данных контейнера


# Deploy Productions:
### Deploy table after deployment

