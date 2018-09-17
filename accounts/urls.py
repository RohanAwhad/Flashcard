from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from mysite import settings

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.UserFormView.as_view(), name='signup'),
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]
