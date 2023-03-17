from django.shortcuts import render
from django.http import JsonResponse
from products.serializers import ProductSerializer

from products.models import Product
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer


# Create your views here.

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    # instance = Product.objects.all().order_by("?").first()
    # data = {}
    # if instance:
    #     data = ProductSerializer(instance).data
    # data = request.data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        print(instance)
        data = serializer.data
        return Response(data)
    return Response({"massage": "BAD Request!"}, status=400)
