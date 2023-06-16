from django.urls import path
from .templates.photo import views

urlpatterns = [
    path('', views.photo_list, name='photo_list'),
]