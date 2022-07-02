from django.urls import path
from storeAPP.api.views import TagView, TagDetailView, BrandView, BrandDetailView
urlpatterns = [
    path('tags/',TagView.as_view(),name='tags_list'),
    path('tag/<int:pk>/', TagDetailView.as_view(), name='tag_detail'),
    path('brands/', BrandView.as_view(), name='berands'),
    path('brand/<int:pk>/',BrandDetailView.as_view(), name='brands_detail'),
    
]
