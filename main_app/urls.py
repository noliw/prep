from django.urls import path
from . import views

urlpatterns = [
    path('', views.DogList.as_view(), name='dog_list'),
    path('create/', views.DogCreate.as_view(), name='dog_create'),
    path('delete/<int:pk>/', views.DogDelete.as_view(), name='dog_delete'),
]