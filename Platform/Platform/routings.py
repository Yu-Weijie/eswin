from django.urls import path
from app01 import dashboard

websocket_urlpatterns = [
    path('dashboard_test/', dashboard.Chart.as_asgi())
]