## Установка

1. Клонировать репозиторий:

    ```python
    git clone https://github.com/katherin-ov/FitFiles_analysis.git
    ```

2. Перейти в папку с проектом:

    ```python
    cd fitness/
    ```

3. Установить виртуальное окружение для проекта:

    ```python
    python -m venv venv
    ```

4. Активировать виртуальное окружение для проекта:

    ```python
    # для OS Lunix и MacOS
    source venv/bin/activate

    # для OS Windows
    source venv/Scripts/activate
    ```

5. Установить зависимости:

    ```python
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

6. Выполнить миграции на уровне проекта:

    ```python
    cd fitness
    python manage.py makemigrations
    python manage.py migrate
    ```

7. Запустить проект локально:

    ```python
    python manage.py runserver

    # адрес запущенного проекта
    http://127.0.0.1:8000
    ```
