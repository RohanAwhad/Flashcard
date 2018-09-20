from django.urls import path
from . import views

app_name = 'study'

urlpatterns = [
    path('', views.SubjectSelectFormView.as_view(), name='index'),
    #path('quiz/', views.quiz, name='quiz'),
    #path('not-enough-cards/', views.quiz, name='not-enough-cards'),
    ]
