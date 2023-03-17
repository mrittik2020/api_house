from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# from django.http import Http404
from django.shortcuts import get_object_or_404


# Only Create --View--> only_POST
class ProductCreateApiView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        cont = serializer.validated_data.get('content')
        if cont is None or cont == "":
            cont = title + "--|-->Edited!"
        serializer.save(content=cont)


product_create_view = ProductCreateApiView.as_view()


# Only Retrieve 1 specific --View--> only_GET
class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_details_view = ProductDetailApiView.as_view()


# Only Retrieve all list --View--> only_GET
class ProductListApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_list_view = ProductListApiView.as_view()


# Only Retrieve all list --View--> only_GET_&&_POST
class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_list_create_view = ProductListCreateApiView.as_view()


@api_view(['GET', 'POST'])
def product_all_views(request, pk=None, *args, **kwargs):
    method = request.method

    if method == 'GET':  # get--Request
        if pk is not None:
            # Details Views---
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        # list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)

    if method == 'POST':  # POST-- request
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)

        return Response({"massage": "BAD Request!"}, status=400)
