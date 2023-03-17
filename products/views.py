from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer


class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_details_view = ProductDetailApiView.as_view()