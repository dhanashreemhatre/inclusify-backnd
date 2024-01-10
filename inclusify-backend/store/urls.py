from django.urls import path
from .views import All_products,ProductDetailAPIView

app_name="store"

urlpatterns=[
    path("products/",All_products.as_view(),name="products"),
    path('products/<int:pk>/',ProductDetailAPIView.as_view())
]