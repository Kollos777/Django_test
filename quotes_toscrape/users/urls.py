from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as CustomLogoutView, views 
app_name = "users"
urlpatterns = [
    path("add_author/", views.add_author, name='add_author'),
    path("login/", views.user_login, name='login'),
    path('register/', views.register, name='register'), 
    path('logout/', views.user_logout, name='logout'),

]
