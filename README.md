Short_url - сервис по сокращению URL.

В данном проекте использовались след. технологии Python 3.8, Django 3.2(фреймворк для разработки вебприложения), sqlite3 

НАСТРОЙКА ПРОЕКТА:

ОСНОВНЫЕ НАСТРОЙКИ ПРОЕКТА:

1)Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/account_name/tz_short_url/

2)Зайдите в short_url/short_url/settings.py и укажите(замените) в переменной DOMAIN ваш домен.

3)Перейти в проект(где находится файл manage.py).

4)Cоздать и активировать виртуальное окружение:

python3 -m venv env

source env/bin/activate

5)Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip

pip install -r requirements.txt

Для запуска сервиса необходимо запустить его веб-приложение:
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

При возникновении вопросов пишите на электронную почту.
Автор: Микутайтис Денис. Почта: denismik92@gmail.com
