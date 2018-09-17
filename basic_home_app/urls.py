from django.urls import path
from . import views

app_name = 'basic_home_app'

urlpatterns = [
    path('', views.index, name='index'),
    ]