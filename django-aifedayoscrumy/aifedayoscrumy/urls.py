from django.urls import path
from aifedayoscrumy import views


urlpatterns = [
    path('', views.index, name = 'index'),
]