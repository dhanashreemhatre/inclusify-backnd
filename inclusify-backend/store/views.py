from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serilizers import ProductSerializer
from .models import Product

# Create your views here.
class All_products(APIView):
    def get(self,request):
        product=Product.objects.all().order_by('?')
        serializer=ProductSerializer(product,many=True)
        return Response(serializer.data)
    