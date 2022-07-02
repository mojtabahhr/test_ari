from rest_framework import generics
from storeAPP.models import (BrandsModel,CategoryModel,GoodsModel,SellerProfile,TagModel)
from storeAPP.api.serializers import (BrandSerializer, TagSerializer, CategorySerializer, GoodsSerializer)


class TagView(generics.ListCreateAPIView):
    queryset = TagModel.objects.all()
    serializer_class = TagSerializer


class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TagModel.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'pk'

class BrandView(generics.ListCreateAPIView):
    queryset = BrandsModel.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'pk'


class BrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BrandsModel.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'pk'
