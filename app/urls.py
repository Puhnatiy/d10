from app import views
from django.urls import path

app_name = 'app'
urlpatterns = [
    path('', views.CarList.as_view(), name='car-list'),
  ]
