from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.ninja_api.urls),  # Шлях до API
]
