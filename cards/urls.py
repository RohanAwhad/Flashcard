from django.urls import path
from . import views

app_name = 'cards'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('subject/add/', views.SubjectCreateView.as_view(), name='add-subject'),
    path('subject/edit/<int:pk>/', views.SubjectUpdate.as_view(), name='edit-subject'),
    path('subject/delete/<int:pk>', views.SubjectDelete.as_view(), name='delete-subject'),

    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/card/add', views.CardCreateView.as_view(), name='add-card'),
    path('<int:fk>/card/edit/<int:pk>', views.CardUpdate.as_view(), name='edit-card'),
    path('<int:fk>/card/delete/<int:pk>', views.CardDelete.as_view(), name='delete-card')
    ]
