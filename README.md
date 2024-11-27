# Тестовое задание на Django для UTF-Tech

## Установка и запуск

Для работы с проектом необходим `Python` версии `3.12` или новее.

1) Клонируйте git репозиторий на ваш компьютер
```commandline
git clone <адрес репозитория>
```
2) Активируйте виртуальное окружение в корне проекта:
```commandline
pip install virtualenv
python -m virtualenv venv 
.\venv\Scripts\activate 
```
3) Установите `poetry` в вашем виртуальном окружении
```commandline
python -m pip install poetry
```
4) Установите зависимости
```commandline
python -m poetry install
```
5) Выполните миграции
```commandline
cd src
python manage.py migrate
```
6) Создайте пользователя для админ-панели
```commandline
python manage.py createsuperuser      
```
7) Заполните бд данными
```commandline
python manage.py populate_food_categories
python manage.py populate_foods
```
Здесь `populate_food_categories` создает разделы меню, а `populate_foods` - позиции в меню

8) Создайте файл `.env` в корне проекта
    1) В `.env` вставьте шаблон из файла `.env_template`
    2) Для `DJANGO_SECRET` установите секретную строку на ваше усмотрение
    3) Для `DEBUG` установите значение `1`, если вам необходимо работать в режиме дебага и `0`, если нет.

9) Запустите сервер
```commandline
python manage.py runserver
```

## Как с этим работать?

* Для начала можете посмотреть, какие позиции меню есть, какие существуют категории,
  а также значения is_publish для позиций меню в админ панели: <br>
  `<локальный адрес сервера>/admin/foods/`
* После, можете отправить `GET` запрос по адресу
  `<локальный адрес сервера>/api/v1/foods`
* Можете сверить `json`-ответ (или ответ на DRF странице) с данными из списка пунктов меню.
  Позиций, где `is_publish=False` ответе нет. Также нет разделов меню, где нет подходящих пунктов.
* Также, можете запустить юнит-тесты, которые проверяют данные, полученные от API с запросом к базе данных напрямую: <br>
  `python manage.py test api`
