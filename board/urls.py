from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home_view, name='home'),
    path('create/', views.create_post_view, name='create_post'),
    path('profile/', views.profile_view, name='profile'),
    path('delete/<int:post_id>/', views.delete_post_view, name='delete_post'),
]