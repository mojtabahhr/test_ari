from django.urls import path, include
from accountAPP.api.views import (SellerProfileView, SellerProfileDetailView, UserView)


urlpatterns = [
    path('users/', UserView.as_view(), name='users_list'),
    path('sellers/',SellerProfileView.as_view(), name='seller_list'),
    path('seller/<int:pk>/', SellerProfileDetailView.as_view(), name='seller_details'),
    
]
