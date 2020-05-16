from django.urls import path
from cowsay_app import views


urlpatterns = [
    path('', views.index),
    path('history/', views.history_data)
]