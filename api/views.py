from django.shortcuts import render
from django.http import JsonResponse
from products.serializers import ProductSerializer

from products.models import Product
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
    return Response(data)
