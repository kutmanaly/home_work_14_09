from django.urls import path
from Product.views import *


urlpatterns = [
    path('Product/', ProductViewSet.as_view(
        {'get': 'list',
         'post': 'create'}
    )),
    path('Product/<int:pk>/', ProductViewSet.as_view(
        {'get': 'retrieve',
         'put': 'update',
         'patch': 'partial_update',
         'delete': 'destroy'}
    )),
]
