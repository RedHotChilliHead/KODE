# Weather API

## Описание

API, которое на HTTP-запрос GET /weather?city=<city_name>, где <city_name> - это название города на английском языке, возвращает текущую температуру в этом городе в градусах Цельсия, атомсферное давление (мм рт.ст.) и скорость ветра (м/c). При первом запросе сервис получает данные о погоде от openweathermap.com, при последующих запросах для этого города в течение получаса запросы на сервис openweathermap.com происходить не должны.

## Установка

1. Клонируйте репозиторий:

```sh
git clone <URL вашего репозитория>
cd <имя папки с вашим репозиторием>
```

2. Установите зависимости:

```sh
pip install -r requirements.txt
```

3. Запустите сервер разработки:

```sh
python manage.py runserver
```

## Использование

Отправьте GET запрос, чтобы получить данные о погоде.

#### URL

```http
`GET /weather?city=<city_name>`
```

#### Пример запроса

```sh
curl -X GET "http://127.0.0.1:8000/weather/?city=Novoaltaysk&appid=a7d16af0e62316b4e1f2772a75c66e57"
```

#### Пример ответа

```json
{
    "Текущая температура С": 14.57,
    "Атомсферное давление (мм рт.ст.)": 750,
    "Скорость ветра (м/c)": 3.74
}
```