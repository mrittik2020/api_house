from django.urls import path
from api.views import api_home

urlpatterns = [
    path('', api_home)  # localhost:8000/api/
]
