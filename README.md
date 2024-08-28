# Weather API

## Описание

Weather API — это сервис, который предоставляет данные о текущей погоде в выбранном городе. 
Отправив HTTP-запрос GET /weather?city=<city_name>, где <city_name> — это название города на английском языке, 
вы получите информацию о текущей температуре в градусах Цельсия, атмосферном давлении (в мм рт. ст.), и скорости ветра (в м/с).

При первом запросе сервис получает данные о погоде из внешнего API (openweathermap.com) и кэширует их. 
В течение следующих 30 минут данные для этого города будут браться из кэша, что снижает нагрузку на API и ускоряет ответы на запросы.

## Шаги установки

1. Клонируйте репозиторий:

```sh
git clone https://github.com/RedHotChilliHead/KODE.git
cd appKODE
```

2. Установите зависимости:

```sh
pip install -r requirements.txt
```

3. Запустите сервер разработки:

```sh
cd appKODE
python manage.py runserver
```
После запуска сервис будет доступен по адресу: http://127.0.0.1:8000/

## Использование

Чтобы получить данные о погоде в определенном городе, отправьте GET запрос на указанный ниже URL.

#### URL

```
`GET /weather?city=<city_name>`
```

#### Пример запроса
Используя curl, отправьте запрос следующим образом:

```sh
curl -X GET "http://127.0.0.1:8000/weather/?city=Novoaltaysk"
```
Примечание: Сервис настроен на работу только с городами России, чтобы исключить двусмысленность в случае городов с одинаковыми названиями в разных странах.

#### Пример ответа
Пример ответа от API на запрос:

```json
{
    "Текущая температура С": 14.57,
    "Атомсферное давление (мм рт.ст.)": 750,
    "Скорость ветра (м/c)": 3.74
}
```