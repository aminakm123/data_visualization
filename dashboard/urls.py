from django.urls import path
from . import views

app_name="dashboard"

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('parse-json/', views.parse_and_store_json, name='parse-json'),
]
