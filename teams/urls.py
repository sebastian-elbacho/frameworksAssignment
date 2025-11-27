from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('edit/', views.edit_profile, name='edit_profile'),   # <== sciezka do edycji
    path('projects/', views.project_list, name='project_list'),
    path('projects/add/', views.add_project, name='add_project'),
]
