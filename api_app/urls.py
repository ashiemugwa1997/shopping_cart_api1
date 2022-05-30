from django.conf.urls import *
from django.urls import path, include
from .views import (CartItemViews, ShoppingCartDetailApiView)

urlpatterns = [
    path('cart-items', CartItemViews.as_view()),
    path('cart-item/<int:cart_id>', ShoppingCartDetailApiView.as_view()),
]