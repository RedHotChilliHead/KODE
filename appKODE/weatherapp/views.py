import json
import requests

from django.core.cache import cache
from django.conf import settings

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class WeatherAPIView(APIView):
    """
    Представление для получения данных о погодных условиях
    Пример запроса: GET /weather?city=<city_name>, где <city_name> - это название города на английском языке
    возвращает текущую температуру в этом городе в градусах Цельсия, атомсферное давление (мм рт.ст.) и скорость ветра (м/c).
    """
    def get(self, request):
        city = request.query_params.get('city')

        if not city:
            return Response(data={'error': 'City not provided'}, status=status.HTTP_400_BAD_REQUEST)

        cache_key = f'weather_{city}'
        data = cache.get(cache_key)

        if not data:
            appid = 'a7d16af0e62316b4e1f2772a75c66e57'
            try:
                response = requests.get(
                    f'http://api.openweathermap.org/data/2.5/weather',
                    params={'q': city, 'units': 'metric', 'APPID': appid},
                    timeout=10  # Таймаут в секундах
                )
                response.raise_for_status()
                response_data = response.json()
                data = {
                    "Текущая температура С": response_data['main']['temp'],
                    "Атомсферное давление (мм рт.ст.)": int(response_data['main']['pressure'] * 0.750064),
                    # гектопаскали переводим в мм.рт.ст.
                    "Скорость ветра (м/c)": response_data['wind']['speed'],
                }

                # Кешируем данные на 30 минут (1800 секунд)
                cache.set(cache_key, data, timeout=1800)
            except requests.exceptions.RequestException as e:
                return Response(data={'error': 'Failed to fetch data from external API', 'details': str(e)},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data=data, status=status.HTTP_200_OK)