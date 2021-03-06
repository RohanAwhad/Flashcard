"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from cards import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('basic_home_app.urls', namespace='basic_home_app')),
    path('cards/', include('cards.urls', namespace='cards')),
    path('study/', include('study.urls', namespace='study')),
    path('', include('dashboard.urls', namespace='dashboard')),
    path('about_us/', include('about_us.urls', namespace='about_us')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/subjects', views.SubjectList.as_view()),
    path('api/cards', views.CardList.as_view()),
    
]


urlpatterns = format_suffix_patterns(urlpatterns)
