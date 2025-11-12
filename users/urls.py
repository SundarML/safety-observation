# users/urls.py
from django.urls import path
from . import views
from .views import CustomLoginView

app_name = 'users'

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('login/', CustomLoginView.as_view(), name='login'),

]
