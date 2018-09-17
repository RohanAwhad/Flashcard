from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('dashboard/', views.index, name='index'),
    path('signup/', views.UserFormView.as_view(), name='signup')
    ]
