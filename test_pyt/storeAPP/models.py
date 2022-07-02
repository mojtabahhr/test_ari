from unicodedata import category
from django.db import models
from accountAPP.models import SellerProfile
# Create your models here.

class CategoryModel(models.Model):
    name = models.CharField(max_length=256)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class TagModel(models.Model):
    name = models.CharField(max_length=256)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class BrandsModel(models.Model):
    category = models.ForeignKey(to=CategoryModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} | {self.category}'

class GoodsModel(models.Model):
    name = models.CharField(max_length=256)
    seller = models.ForeignKey(to=SellerProfile, on_delete=models.CASCADE)
    brand = models.ForeignKey(to=BrandsModel, on_delete=models.CASCADE)
    price = models.IntegerField()
    # info = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} | {self.seller}'


# class PriceModel(models.Model):
#     pass

