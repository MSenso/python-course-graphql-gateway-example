GraphQL API Gateway
===================

Пример реализации GraphQL API шлюза для взаимодействия с микросервисами.

Зависимости
===========
Установите соответствующее программное обеспечение:

1. [Docker Desktop](https://www.docker.com).
2. [Git](https://github.com/git-guides/install-git).
3. [PyCharm](https://www.jetbrains.com/ru-ru/pycharm/download) (опционально).


Установка
=========
Клонируйте репозиторий на свой компьютер:

.. code-block::console
    git clone https://github.com/mnv/python-course-graphql-gateway

1. Для настройки приложения скопируйте `.env.sample` в файл `.env`:
.. code-block::console
    cp .env.sample .env

Этот файл содержит переменные окружения, значения которых будут общими для всего приложения.
Файл-образец (`.env.sample`) содержит набор переменных со значениями по умолчанию.
Поэтому он может быть настроен в зависимости от окружения.

2. Соберите контейнер с помощью Docker Compose:
.. code-block::console
    docker compose build

Эта команда должна быть запущена из корневого каталога, в котором находится `Dockerfile`.
Вам также необходимо собрать docker-контейнер заново в случае, если вы обновили `requirements.txt`.

3. Чтобы запустить проект внутри контейнера Docker:
.. code-block::console
    docker compose up

После запуска контейнеров сервер запускается по адресу [http://127.0.0.1:8000/graphql](http://127.0.0.1:8000/graphql). Вы можете открыть его в браузере.


Использование
=============
Этот проект предоставляет фикстуры для тестирования GraphQL. Фикстуры находятся в `src/fixtures`.
Там находятся JSON-файлы для информации о любимых местах и странах.
Приложение GraphQL использует эти фикстуры для эмуляции ответов REST API.

Пример запроса для получения списка любимых мест:

.. code-block::graphql
    query {
      places {
        latitude
        longitude
        description
        city
        locality
      }
    }

Пример запроса для получения списка любимых мест с информацией о странах:

.. code-block::graphql
    query {
      places {
        latitude
        longitude
        description
        city
        locality
        country {
          name
          capital
          alpha2code
          alpha3code
          capital
          region
          subregion
          population
          latitude
          longitude
          demonym
          area
          numericCode
          flag
          currencies
          languages
        }
      }
    }

Этот запрос запросит дополнительную информацию о связанных странах оптимальным способом,
используя загрузчики данных, чтобы предотвратить проблему N + 1 запросов.

Автоматизация
=============

Проект содержит специальный `Makefile`, который предоставляет ярлыки для набора команд:

1. Создайте контейнер Docker:

.. code-block::console
    make build

2. Сгенерируйте документацию Sphinx:

.. code-block::console
    make docs-html

3. Автоформатирование исходного кода:

.. code-block::console
    make format

4. Статический анализ (линтеры):

.. code-block::console
    make lint

5. Автотесты:

.. code-block::console
    make test

Отчет о покрытии тестами будет расположен по адресу `src/htmlcov/index.html`.
Таким образом, вы можете оценить качество покрытия автоматизированных тестов.

6. Запуск автоформата, линтеров и тестов одной командой:

.. code-block::console
    make all

Выполните эти команды из исходного каталога, в котором находится `Makefile`.

Документация
=============

Проект интегрирован с движком документации [Sphinx](https://www.sphinx-doc.org/en/master/).
Он позволяет создавать документацию из исходного кода.
Таким образом, исходный код должен содержать документацию в формате [reStructuredText](https://docutils.sourceforge.io/rst.html).

Для создания HTML документации выполните эту команду из каталога исходников, где находится `Makefile`:
.. code-block::console
make docs-html


После генерации документацию можно открыть из файла `docs/build/html/index.html`.

Модели
------

.. automodule:: models.places
    :members:

.. automodule:: models.countries
    :members:

.. automodule:: models.news
    :members:

Сервисы
-------

.. automodule:: services.places
    :members:

.. automodule:: services.countries
    :members:

.. automodule:: services.news
    :members:

Схема
-----

.. automodule:: schema
    :members:


Context
-------

.. automodule:: context
    :members:

Data loaders
------------

.. automodule:: dataloaders
    :members:

Настройки
---------

.. automodule:: settings
    :members:
