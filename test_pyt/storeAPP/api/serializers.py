from pyexpat import model
from attr import field
from rest_framework import serializers
from storeAPP.models import (TagModel, BrandsModel, CategoryModel, GoodsModel, SellerProfile)

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagModel
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandsModel
        fielsd = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =CategoryModel
        fields = "__all__"

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsModel
        fields = '__all__'