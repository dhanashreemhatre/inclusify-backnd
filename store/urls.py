from django.urls import path
from .views import All_products


urlpatterns=[
    path("products",All_products.as_view(),name="products"),
]