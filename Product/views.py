from rest_framework import viewsets
from rest_framework.generics import *
from Product.models import Product
from Product.serializers import ProductsListSerializer, ProductDetailSerializer, CreateProductSerializer


class ProductsListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsListSerializer


class ProductDetailsView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsListSerializer


class CreateProductView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer


class UpdateProductView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer


class DeleteProductView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductsListSerializer
        elif self.action == 'retrieve':
            return  ProductDetailSerializer
        return CreateProductSerializer

