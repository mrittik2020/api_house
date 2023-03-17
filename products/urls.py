from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_create_view),  # POST--> 127.0.0.1:8000/api/products/
    path('<int:pk>/', views.product_details_view),  # GET--> 127.0.0.1:8000/api/products/{any primary key value}
    path('list/', views.product_list_view),  # GET--> 127.0.0.1:8000/api/products/list
    path('list_create/', views.product_list_create_view),  # GET_AND_POST  127.0.0.1:8000/api/product/list_create/

    # custom API Django
    # GET_AND_POST  127.0.0.1:8000/api/product/custom/
    path('custom/', views.product_all_views),
    path('custom/<int:pk>/', views.product_all_views)

]
