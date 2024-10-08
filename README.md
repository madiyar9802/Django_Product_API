# Django_Product_API

Django_Product_API — это REST API, разработанный на Django и Django Rest Framework для управления данными о продуктах, фотографиях и городах. API позволяет создавать, получать и фильтровать продукты и связанные с ними данные.

## Основные возможности

- Управление продуктами
- Добавление ссылок на фотографии, связанных с продуктами и городами, фильтрация ссылок по городу

## Установка и запуск

Для запуска приложения выполните следующие шаги:

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/madiyar9802/Django_Product_API.git
   cd Django_Product_API
   ```

2. **Установите зависимости используя poetry:**

   ```bash
   poetry shell
   poetry install
   ```
   
    **Установите зависимости используя pip:**
  
     ```bash
     python -m venv venv
     source venv/bin/activate
     # Для Windows используйте: venv\Scripts\activate
     pip install -r requirements.txt
     ```
   

4. **Примените миграции базы данных:**

   ```bash
   cd cities_project
   python manage.py migrate
   ```

5. **Запустите сервер разработки:**

   ```bash
   python manage.py runserver
   ```

После этого приложение будет доступно по адресу `http://localhost:8000/api/products`.

## Маршруты API

Приложение предоставляет следующие конечные точки:

| Метод | Конечная точка   | Описание                                         |
|-------|------------------|--------------------------------------------------|
| GET   | `/products/`     | Получить список всех продуктов                   |
| POST  | `/products/`     | Создать новый продукт                            |
| GET   | `/photo_link/`   | Получить ссылки на фото |
| POST  | `/photo_link/`   | Создать новую ссылку на фото                         |
| GET   | `/city/`         | Получить список всех городов                     |
| POST  | `/city/`         | Создать новый город                              |

## Тестирование

Проект включает тесты для проверки функциональности API. Тесты написаны с использованием фреймворка Django Test и Django Rest Framework Test.

### Запуск тестов

Чтобы запустить тесты, выполните следующую команду:

```bash
python manage.py test
```

Тесты охватывают:

- **Модельные тесты:** Проверка создания и правильности атрибутов для моделей `Product`, `City` и `PhotoLink`.
- **API тесты:** Проверка конечных точек API, включая создание и получение продуктов и ссылок на фотографии.

## Пример запроса

Вот пример запроса к API для получения списка продуктов:

```bash
curl -X GET http://localhost:8000/api/products/
```

Или с использованием фильтрации по городу:

```bash
curl -X GET http://localhost:8000/api/products/ -H "City: <City_ID>"
```

---

Этот `README.md` содержит всю необходимую информацию для быстрого развертывания и тестирования проекта Django_Product_API.
