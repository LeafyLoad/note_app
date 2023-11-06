# README.MD

Перед запуском нужно установить необходимые библиотеки(pylint)
с помощью

**pip install -r requirements.txt**

## Краткое описание

%Имеется 4 файла:%

**main.py** - точка входа в приложение, запускаем его для работы приложения

**database.py** - модуль работы с базой данных, где описаны все основные функции

**menu_executor.py** - модуль отрисовки меню и связи модуля с файлом **database.py**

**pylint_tests.py** - **pylint** тесты на соответствие стандартам написания кода PEP-8, можно запустить для того чтобы увидеть результаты, по всем файлам 10/10

рекомендую запускать не через pycharm, а через обычную консоль, красивее будет выглядеть

## Примечание

Кроме pylint дополнительные библиотеки не используются, только встроенные в python, делал на 3.11, но на любом питоне 3 версии будет работать, но все же рекомендую использовать версию посвежее
