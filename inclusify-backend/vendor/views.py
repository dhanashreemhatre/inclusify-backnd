from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from accounts.models import Account
from .seralizers import VendorSerializer,VendorProductSerializer
from django.contrib.auth import get_user_model
from .models import Vendor
from rest_framework.permissions import IsAuthenticated  # Import the necessary permission
from rest_framework.decorators import permission_classes


# Create your views here.
class VendorRegistratonAPIView(APIView):
    def post(self,request):
        serializer=VendorSerializer(data=request.data)
        if serializer.is_valid():
            # user=get_user_model().objects.create_user(**serializer.validated_data.pop('user'))
            vendor=Vendor.objects.create(**serializer.validated_data)
            return Response(VendorSerializer(vendor).data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    



# @permission_classes([IsAuthenticated])  # Ensure only authenticated vendors can add products
class VendorProductCreateAPIView(APIView):
    def post(self, request):
        serializer = VendorProductSerializer(data=request.data)  # Use your serializer (e.g., VendorProductSerializer)
        if serializer.is_valid():
            # Assign the vendor to the product before saving (you might use the logged-in user/vendor)
            serializer.validated_data['vendor'] = request.user.vendor  # Assuming vendor info is in the request's user object

            # Create the product
            product = serializer.save()

            return Response(VendorProductSerializer(product).data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
