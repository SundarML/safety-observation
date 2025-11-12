# users/urls.py
from django.urls import path, include
from . import views
from .views import CustomLoginView
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', include('observations.urls')),

]
