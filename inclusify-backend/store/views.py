from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serilizers import ProductSerializer
from .models import Product
from rest_framework import status

# Create your views here.
class All_products(APIView):
    def get(self,request):
        product=Product.objects.all().order_by('?')
        serializer=ProductSerializer(product,many=True)
        return Response(serializer.data)

class ProductDetailAPIView(APIView):
    def get(self,request,pk):
        try:
            product_detail=Product.objects.get(pk=pk)
            serailizer=ProductSerializer(product_detail)
            return Response(serailizer.data)
        except:
            return Response({'error':'Product not found'},status=status.HTTP_404_NOT_FOUND)


