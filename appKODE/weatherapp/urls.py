from django.urls import path, include
from .views import WeatherAPIView

app_name = "weatherapp"

# router = DefaultRouter()
# router.register(r'suppliers', SupplierViewSet)
#
urlpatterns = [
    path('', WeatherAPIView.as_view(), name='weather'),
]