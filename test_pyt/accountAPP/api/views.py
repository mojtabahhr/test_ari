from rest_framework import generics
from accountAPP.models import SellerProfile, User
from accountAPP.api.serializers import SellerProfileSerializer, UserSerialzer


class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerialzer
    queryset = User.objects.all()

class SellerProfileView(generics.ListCreateAPIView):
    serializer_class = SellerProfileSerializer
    queryset = SellerProfile.objects.all()

class SellerProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SellerProfileSerializer
    queryset = SellerProfile.objects.all()
    lookup_field = 'pk'