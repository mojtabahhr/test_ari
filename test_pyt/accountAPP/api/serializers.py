from pyexpat import model
from rest_framework import serializers
from accountAPP.models import SellerProfile, User


class SellerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerProfile
        fields = '__all__'
    
class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['username','is_staff', 'is_active', 'is_superuser','username','first_name','last_name','email','password']
