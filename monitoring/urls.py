from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.map_view, name='map_view'),
    path('schools/', views.school_list, name='school_list'),
    path('schools/add/', views.add_school, name='add_school'),
    path('schools/<int:school_id>/edit/', views.edit_school, name='edit_school'),
    path('schools/<int:school_id>/delete/', views.delete_school, name='delete_school'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.custom_logout, name='custom_logout'),
]


