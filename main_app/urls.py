from django.urls import path
from . import views

urlpatterns = [
    path('', views.ItemList.as_view(), name='item_list'),
    path('items/create/', views.ItemCreate.as_view(), name='item_create'),
    path('items/<int:pk>/delete', views.ItemDelete.as_view(), name='item_delete'),
]