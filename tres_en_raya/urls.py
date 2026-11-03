from django.urls import path
from . import views

urlpatterns = [
    path('', views.tres_en_raya, name='tres_en_raya'),
]