from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('cart/', views.cart),
    path('shippinginfo/', views.shippinginfo),
    path('final/', views.final),
    path('delete/<int:pk>/', views.delete),
]
