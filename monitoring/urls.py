from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_view, name='map_view'),
    path('schools/', views.school_list, name='school_list'),
    path('schools/add/', views.add_school, name='add_school'),
    path('schools/<int:school_id>/edit/', views.edit_school, name='edit_school'),
    path('schools/<int:school_id>/delete/', views.delete_school, name='delete_school'),
    path('logout/', views.custom_logout, name='custom_logout'),
]

