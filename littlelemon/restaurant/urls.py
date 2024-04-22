from django.contrib import admin 
from django.urls import path 
from .views import index, MenuItemsView, SingleMenuItemView, BookingItemsView, SingleBookingItemView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [ 
    path('', index, name='index'), 
    path('menu-items/', MenuItemsView.as_view(), name='menu-items-list'),
    path('menu-items/<int:pk>/', SingleMenuItemView.as_view(), name='single-menu-item'),
    path('booking-items/', BookingItemsView.as_view(), name='booking-items-list'),
    path('booking-items/<int:pk>/', SingleBookingItemView.as_view(), name='single-booking-item'),
    path('api-token-auth/', obtain_auth_token)
]