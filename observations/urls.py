# observations/urls.py
from django.urls import path
from . import views

app_name = 'observations'

urlpatterns = [
    path('', views.ObservationListView.as_view(), name='observation_list'),
    path('new/', views.ObservationCreateView.as_view(), name='create'),
    path('<int:pk>/', views.ObservationDetailView.as_view(), name='detail'),
    path('<int:pk>/rectify/', views.RectificationUpdateView.as_view(), name='rectify'),
    path('<int:pk>/verify/', views.VerificationView.as_view(), name='verify'),
]

